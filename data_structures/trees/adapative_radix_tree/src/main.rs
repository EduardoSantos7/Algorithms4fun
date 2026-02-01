use std::collections::BTreeMap;
use std::time::Instant;

fn u64_to_key_bytes(x: u64) -> [u8; 8] {
    x.to_be_bytes()
}

// Simple xorshift64 PRNG (deterministic, no crates)
#[derive(Clone)]
struct XorShift64 {
    state: u64,
}
impl XorShift64 {
    fn new(seed: u64) -> Self {
        Self { state: seed.max(1) }
    }
    fn next_u64(&mut self) -> u64 {
        let mut x = self.state;
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
        self.state = x;
        x
    }
}

// ---------------- ART (educational) ----------------

#[derive(Debug)]
enum Node {
    Leaf { key: Vec<u8>, value: u64 },
    Inner(InnerNode),
}

#[derive(Debug)]
struct InnerNode {
    prefix: Vec<u8>,
    kind: NodeKind,
}

#[derive(Debug)]
enum NodeKind {
    N4(Vec<(u8, Box<Node>)>), // sorted by byte
    N16(Vec<(u8, Box<Node>)>), // sorted by byte
    N48 {
        idx: [i16; 256],
        children: Vec<Box<Node>>,
    },
    N256(Vec<Option<Box<Node>>>), // len 256
}

impl InnerNode {
    fn new_n4(prefix: Vec<u8>) -> Self {
        Self {
            prefix,
            kind: NodeKind::N4(Vec::new()),
        }
    }

    fn find_child(&self, b: u8) -> Option<&Box<Node>> {
        match &self.kind {
            NodeKind::N4(v) | NodeKind::N16(v) => v
                .binary_search_by_key(&b, |(k, _)| *k)
                .ok()
                .map(|i| &v[i].1),
            NodeKind::N48 { idx, children } => {
                let p = idx[b as usize];
                if p < 0 {
                    None
                } else {
                    Some(&children[p as usize])
                }
            }
            NodeKind::N256(children) => children[b as usize].as_ref(),
        }
    }

    fn find_child_mut(&mut self, b: u8) -> Option<&mut Box<Node>> {
        match &mut self.kind {
            NodeKind::N4(v) | NodeKind::N16(v) => v
                .binary_search_by_key(&b, |(k, _)| *k)
                .ok()
                .map(move |i| &mut v[i].1),
            NodeKind::N48 { idx, children } => {
                let p = idx[b as usize];
                if p < 0 {
                    None
                } else {
                    Some(&mut children[p as usize])
                }
            }
            NodeKind::N256(children) => children[b as usize].as_mut(),
        }
    }

    fn insert_child(&mut self, b: u8, child: Box<Node>) {
        match &mut self.kind {
            NodeKind::N4(v) => {
                let pos = v
                    .binary_search_by_key(&b, |(k, _)| *k)
                    .unwrap_or_else(|p| p);

                if pos < v.len() && v[pos].0 == b {
                    v[pos].1 = child;
                    return;
                }

                v.insert(pos, (b, child));
                if v.len() > 4 {
                    self.grow();
                }
            }
            NodeKind::N16(v) => {
                let pos = v
                    .binary_search_by_key(&b, |(k, _)| *k)
                    .unwrap_or_else(|p| p);

                if pos < v.len() && v[pos].0 == b {
                    v[pos].1 = child;
                    return;
                }

                v.insert(pos, (b, child));
                if v.len() > 16 {
                    self.grow();
                }
            }
            NodeKind::N48 { idx, children } => {
                let cur = idx[b as usize];
                if cur >= 0 {
                    children[cur as usize] = child;
                    return;
                }
                idx[b as usize] = children.len() as i16;
                children.push(child);
                if children.len() > 48 {
                    self.grow();
                }
            }
            NodeKind::N256(children) => {
                children[b as usize] = Some(child);
            }
        }
    }

    fn grow(&mut self) {
        self.kind = match std::mem::replace(&mut self.kind, NodeKind::N4(Vec::new())) {
            NodeKind::N4(v) => {
                // N4 -> N16 (same representation, higher cap)
                NodeKind::N16(v)
            }
            NodeKind::N16(v) => {
                // N16 -> N48
                let mut idx = [-1i16; 256];
                let mut children = Vec::with_capacity(v.len());
                for (k, ch) in v {
                    idx[k as usize] = children.len() as i16;
                    children.push(ch);
                }
                NodeKind::N48 { idx, children }
            }
            NodeKind::N48 { idx, children } => {
                // N48 -> N256
                // Avoid vec![None; 256] which would require Option<Box<Node>>: Clone.
                let mut arr: Vec<Option<Box<Node>>> =
                    vec![(); 256].into_iter().map(|_| None).collect();

                // Put children into an Option pool so we can move them with take()
                let mut pool: Vec<Option<Box<Node>>> = children.into_iter().map(Some).collect();

                for b in 0..256usize {
                    let p = idx[b];
                    if p >= 0 {
                        arr[b] = pool[p as usize].take(); // move, no clone
                    }
                }

                NodeKind::N256(arr)
            }
            NodeKind::N256(v) => NodeKind::N256(v),
        };
    }
}

#[derive(Default)]
struct ArtMap {
    root: Option<Box<Node>>,
}

impl ArtMap {
    fn get(&self, key: &[u8]) -> Option<u64> {
        let mut node = self.root.as_ref()?;
        let mut depth = 0usize;

        loop {
            match node.as_ref() {
                Node::Leaf { key: k, value } => {
                    return if k.as_slice() == key {
                        Some(*value)
                    } else {
                        None
                    }
                }
                Node::Inner(inner) => {
                    if !inner.prefix.is_empty() {
                        let end = depth + inner.prefix.len();
                        if end > key.len() || &key[depth..end] != inner.prefix.as_slice() {
                            return None;
                        }
                        depth = end;
                    }
                    if depth >= key.len() {
                        return None;
                    }
                    let b = key[depth];
                    node = inner.find_child(b)?;
                    depth += 1;
                }
            }
        }
    }

    fn insert(&mut self, key: Vec<u8>, value: u64) {
        self.root = Some(Self::insert_rec(self.root.take(), key, value, 0));
    }

    fn common_prefix(a: &[u8], b: &[u8], start: usize) -> usize {
        let mut i = start;
        let n = a.len().min(b.len());
        while i < n && a[i] == b[i] {
            i += 1;
        }
        i - start
    }

    fn insert_rec(node: Option<Box<Node>>, key: Vec<u8>, value: u64, depth: usize) -> Box<Node> {
        match node {
            None => Box::new(Node::Leaf { key, value }),
            Some(mut boxed) => match boxed.as_mut() {
                Node::Leaf { key: k2, value: v2 } => {
                    if k2.as_slice() == key.as_slice() {
                        *v2 = value;
                        return boxed;
                    }
                    // expand leaf into Node4 (lazy expansion)
                    let common = Self::common_prefix(k2, &key, depth);
                    let mut inner = InnerNode::new_n4(key[depth..depth + common].to_vec());
                    let d2 = depth + common;

                    let old_edge = k2[d2];
                    let new_edge = key[d2];

                    let old_leaf = boxed; // reuse old leaf box
                    inner.insert_child(old_edge, old_leaf);
                    inner.insert_child(new_edge, Box::new(Node::Leaf { key, value }));
                    Box::new(Node::Inner(inner))
                }
                Node::Inner(inner) => {
                    // prefix mismatch split
                    if !inner.prefix.is_empty() {
                        let mut p = 0usize;
                        while p < inner.prefix.len()
                            && depth + p < key.len()
                            && inner.prefix[p] == key[depth + p]
                        {
                            p += 1;
                        }
                        if p != inner.prefix.len() {
                            let mut new_inner = InnerNode::new_n4(inner.prefix[..p].to_vec());
                            let old_edge = inner.prefix[p];
                            let new_edge = key[depth + p];

                            inner.prefix = inner.prefix[p + 1..].to_vec();
                            let old_node = boxed; // existing subtree becomes child

                            new_inner.insert_child(old_edge, old_node);
                            new_inner.insert_child(new_edge, Box::new(Node::Leaf { key, value }));
                            return Box::new(Node::Inner(new_inner));
                        }
                    }

                    let d = depth + inner.prefix.len();
                    if d >= key.len() {
                        return boxed;
                    }

                    let b = key[d];
                    if inner.find_child(b).is_none() {
                        inner.insert_child(b, Box::new(Node::Leaf { key, value }));
                        return boxed;
                    }

                    // recurse into existing child
                    let child = inner.find_child_mut(b).unwrap();

                    // move child out temporarily (placeholder leaf won't be observed because we overwrite)
                    let taken = std::mem::replace(
                        child,
                        Box::new(Node::Leaf {
                            key: Vec::new(),
                            value: 0,
                        }),
                    );
                    let new_child = Self::insert_rec(Some(taken), key, value, d + 1);
                    *child = new_child;

                    boxed
                }
            },
        }
    }
}

fn gen_keys(n: usize, mode: &str, seed: u64) -> Vec<u64> {
    if mode == "dense" {
        let mut v: Vec<u64> = (0..n as u64).collect();
        let mut rng = XorShift64::new(seed);

        // Fisher-Yates shuffle
        for i in (1..v.len()).rev() {
            let j = (rng.next_u64() as usize) % (i + 1);
            v.swap(i, j);
        }
        return v;
    }

    // sparse: pseudo-random u64 (duplicates possible; fine for a benchmark)
    let mut rng = XorShift64::new(seed);
    (0..n).map(|_| rng.next_u64()).collect()
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let n: usize = args.get(1).and_then(|s| s.parse().ok()).unwrap_or(200_000);
    let lookups: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(200_000);
    let mode = args.get(3).map(|s| s.as_str()).unwrap_or("dense");

    let keys = gen_keys(n, mode, 123);
    let lookup_keys = keys
        .iter()
        .take(lookups.min(keys.len()))
        .cloned()
        .collect::<Vec<_>>();

    // ART insert
    let mut art = ArtMap::default();
    let t0 = Instant::now();
    for &k in &keys {
        art.insert(u64_to_key_bytes(k).to_vec(), k);
    }
    let t1 = t0.elapsed();

    // BTreeMap insert
    let mut bt = BTreeMap::new();
    let t2s = Instant::now();
    for &k in &keys {
        bt.insert(k, k);
    }
    let t2 = t2s.elapsed();

    // correctness spot-check
    for &k in lookup_keys.iter().take(10_000.min(lookup_keys.len())) {
        let a = art.get(&u64_to_key_bytes(k));
        let b = bt.get(&k).cloned();
        assert_eq!(a, b);
    }

    // ART lookup
    let t3s = Instant::now();
    let mut acc1: u64 = 0;
    for &k in &lookup_keys {
        acc1 ^= art.get(&u64_to_key_bytes(k)).unwrap_or(0);
    }
    let t3 = t3s.elapsed();

    // BTreeMap lookup
    let t4s = Instant::now();
    let mut acc2: u64 = 0;
    for &k in &lookup_keys {
        acc2 ^= bt.get(&k).cloned().unwrap_or(0);
    }
    let t4 = t4s.elapsed();

    assert_eq!(acc1, acc2);

    println!("Mode: {mode}, n={n}, lookups={}", lookup_keys.len());
    println!("Insert  ART:   {:.3?}", t1);
    println!("Insert  BTree: {:.3?}", t2);
    println!("Lookup  ART:   {:.3?}", t3);
    println!("Lookup  BTree: {:.3?}", t4);
}
