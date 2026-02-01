#!/usr/bin/env python3
"""
art_vs_avl.py

Educational Adaptive Radix Tree (ART) + AVL baseline + benchmark/test runner.

- Keys: u64 (converted to big-endian bytes; binary-comparable for unsigned ints).
- Values: arbitrary (we use int for tests).
- Implements: insert/get for ART and AVL.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any, List
import argparse
import random
import time
import bisect


# ---------------------------
# Binary-comparable key helpers
# ---------------------------

def u64_to_art_key(x: int) -> bytes:
    # For unsigned ints, big-endian byte order gives lexicographic order
    # (matches the paper's endianness point). :contentReference[oaicite:12]{index=12}
    return int(x & ((1 << 64) - 1)).to_bytes(8, "big")

def i64_to_art_key(x: int) -> bytes:
    # Signed reorder: flip sign bit then big-endian. :contentReference[oaicite:13]{index=13}
    ux = (x & ((1 << 64) - 1)) ^ (1 << 63)
    return ux.to_bytes(8, "big")


# ---------------------------
# ART Node definitions
# ---------------------------

class ARTNode:
    __slots__ = ("prefix",)

    def __init__(self, prefix: bytes = b""):
        self.prefix = prefix  # compressed path bytes (pessimistic path compression)

    def find_child(self, b: int) -> Optional["ARTNode"]:
        raise NotImplementedError

    def set_child(self, b: int, child: "ARTNode") -> "ARTNode":
        """Insert or replace child. Returns (possibly new) node if it grew."""
        raise NotImplementedError

    def iter_children_items(self):
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    def grow(self) -> "ARTNode":
        raise NotImplementedError


class Leaf(ARTNode):
    __slots__ = ("key", "value")

    def __init__(self, key: bytes, value: Any):
        super().__init__(b"")
        self.key = key
        self.value = value


class Node4(ARTNode):
    __slots__ = ("keys", "children")

    def __init__(self, prefix: bytes = b""):
        super().__init__(prefix)
        self.keys: List[int] = []
        self.children: List[ARTNode] = []

    def find_child(self, b: int) -> Optional[ARTNode]:
        for i, kb in enumerate(self.keys):
            if kb == b:
                return self.children[i]
        return None

    def set_child(self, b: int, child: ARTNode) -> ARTNode:
        for i, kb in enumerate(self.keys):
            if kb == b:
                self.children[i] = child
                return self
        # insert sorted
        pos = bisect.bisect_left(self.keys, b)
        self.keys.insert(pos, b)
        self.children.insert(pos, child)
        if self.is_full():
            return self.grow()
        return self

    def iter_children_items(self):
        return zip(self.keys, self.children)

    def is_full(self) -> bool:
        return len(self.keys) > 4  # allow temporary overflow then grow

    def grow(self) -> ARTNode:
        n = Node16(self.prefix)
        for b, ch in self.iter_children_items():
            n.keys.append(b)
            n.children.append(ch)
        return n


class Node16(ARTNode):
    __slots__ = ("keys", "children")

    def __init__(self, prefix: bytes = b""):
        super().__init__(prefix)
        self.keys: List[int] = []
        self.children: List[ARTNode] = []

    def find_child(self, b: int) -> Optional[ARTNode]:
        i = bisect.bisect_left(self.keys, b)
        if i < len(self.keys) and self.keys[i] == b:
            return self.children[i]
        return None

    def set_child(self, b: int, child: ARTNode) -> ARTNode:
        i = bisect.bisect_left(self.keys, b)
        if i < len(self.keys) and self.keys[i] == b:
            self.children[i] = child
            return self
        self.keys.insert(i, b)
        self.children.insert(i, child)
        if self.is_full():
            return self.grow()
        return self

    def iter_children_items(self):
        return zip(self.keys, self.children)

    def is_full(self) -> bool:
        return len(self.keys) > 16

    def grow(self) -> ARTNode:
        n = Node48(self.prefix)
        for b, ch in self.iter_children_items():
            n._add_child_no_grow(b, ch)
        return n


class Node48(ARTNode):
    __slots__ = ("child_index", "children")

    EMPTY = -1

    def __init__(self, prefix: bytes = b""):
        super().__init__(prefix)
        self.child_index = [self.EMPTY] * 256
        self.children: List[ARTNode] = []

    def find_child(self, b: int) -> Optional[ARTNode]:
        idx = self.child_index[b]
        if idx == self.EMPTY:
            return None
        return self.children[idx]

    def _add_child_no_grow(self, b: int, child: ARTNode):
        # assumes not already present
        self.child_index[b] = len(self.children)
        self.children.append(child)

    def set_child(self, b: int, child: ARTNode) -> ARTNode:
        idx = self.child_index[b]
        if idx != self.EMPTY:
            self.children[idx] = child
            return self
        self._add_child_no_grow(b, child)
        if self.is_full():
            return self.grow()
        return self

    def iter_children_items(self):
        # expensive but fine for educational build
        for b in range(256):
            idx = self.child_index[b]
            if idx != self.EMPTY:
                yield b, self.children[idx]

    def is_full(self) -> bool:
        return len(self.children) > 48

    def grow(self) -> ARTNode:
        n = Node256(self.prefix)
        for b, ch in self.iter_children_items():
            n.children[b] = ch
        return n


class Node256(ARTNode):
    __slots__ = ("children",)

    def __init__(self, prefix: bytes = b""):
        super().__init__(prefix)
        self.children: List[Optional[ARTNode]] = [None] * 256

    def find_child(self, b: int) -> Optional[ARTNode]:
        return self.children[b]

    def set_child(self, b: int, child: ARTNode) -> ARTNode:
        self.children[b] = child
        return self  # no grow

    def iter_children_items(self):
        for b, ch in enumerate(self.children):
            if ch is not None:
                yield b, ch

    def is_full(self) -> bool:
        return False

    def grow(self) -> ARTNode:
        return self


# ---------------------------
# ART Map wrapper (insert/get)
# ---------------------------

class ARTMap:
    def __init__(self):
        self.root: Optional[ARTNode] = None

    @staticmethod
    def _common_prefix(a: bytes, b: bytes, start: int) -> int:
        i = start
        n = min(len(a), len(b))
        while i < n and a[i] == b[i]:
            i += 1
        return i - start

    def get(self, key: bytes) -> Optional[Any]:
        node = self.root
        depth = 0
        while node is not None:
            if isinstance(node, Leaf):
                return node.value if node.key == key else None  # lazy expansion leaf check :contentReference[oaicite:14]{index=14}
            # prefix check (pessimistic path compression) :contentReference[oaicite:15]{index=15}
            pref = node.prefix
            if pref:
                if key[depth:depth + len(pref)] != pref:
                    return None
                depth += len(pref)
            if depth >= len(key):
                return None
            node = node.find_child(key[depth])
            depth += 1
        return None

    def insert(self, key: bytes, value: Any) -> None:
        self.root = self._insert(self.root, key, value, 0)

    def _insert(self, node: Optional[ARTNode], key: bytes, value: Any, depth: int) -> ARTNode:
        if node is None:
            return Leaf(key, value)

        if isinstance(node, Leaf):
            if node.key == key:
                node.value = value
                return node
            # expand leaf into an inner node (lazy expansion case) :contentReference[oaicite:16]{index=16}
            new = Node4()
            common = self._common_prefix(node.key, key, depth)
            new.prefix = key[depth:depth + common]
            depth2 = depth + common
            new = new.set_child(node.key[depth2], node)
            new = new.set_child(key[depth2], Leaf(key, value))
            return new

        # inner node: handle prefix mismatch split (path compression logic) :contentReference[oaicite:17]{index=17}
        pref = node.prefix
        if pref:
            # compute matching prefix bytes
            maxcmp = min(len(pref), len(key) - depth)
            p = 0
            while p < maxcmp and pref[p] == key[depth + p]:
                p += 1
            if p != len(pref):
                # split node
                new = Node4(prefix=pref[:p])
                # old edge byte is pref[p]
                old_edge = pref[p]
                # new edge byte is key[depth + p]
                new_edge = key[depth + p]
                # adjust existing node's prefix: drop p+1 (byte becomes edge label)
                node.prefix = pref[p + 1 :]
                new = new.set_child(old_edge, node)
                new = new.set_child(new_edge, Leaf(key, value))
                return new
            depth += len(pref)

        if depth >= len(key):
            # shouldn't happen for fixed-length keys
            return node

        b = key[depth]
        child = node.find_child(b)
        if child is None:
            node2 = node.set_child(b, Leaf(key, value))
            return node2
        else:
            new_child = self._insert(child, key, value, depth + 1)
            node2 = node.set_child(b, new_child)
            return node2


# ---------------------------
# AVL tree baseline
# ---------------------------

@dataclass
class AVLNode:
    key: int
    value: Any
    height: int = 1
    left: Optional["AVLNode"] = None
    right: Optional["AVLNode"] = None


def _h(n: Optional[AVLNode]) -> int:
    return n.height if n else 0

def _upd(n: AVLNode) -> None:
    n.height = 1 + max(_h(n.left), _h(n.right))

def _bf(n: AVLNode) -> int:
    return _h(n.left) - _h(n.right)

def _rot_r(y: AVLNode) -> AVLNode:
    x = y.left
    assert x is not None
    t2 = x.right
    x.right = y
    y.left = t2
    _upd(y)
    _upd(x)
    return x

def _rot_l(x: AVLNode) -> AVLNode:
    y = x.right
    assert y is not None
    t2 = y.left
    y.left = x
    x.right = t2
    _upd(x)
    _upd(y)
    return y

class AVLMap:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def get(self, k: int) -> Optional[Any]:
        n = self.root
        while n:
            if k == n.key:
                return n.value
            n = n.left if k < n.key else n.right
        return None

    def insert(self, k: int, v: Any) -> None:
        self.root = self._ins(self.root, k, v)

    def _ins(self, n: Optional[AVLNode], k: int, v: Any) -> AVLNode:
        if n is None:
            return AVLNode(k, v)
        if k < n.key:
            n.left = self._ins(n.left, k, v)
        elif k > n.key:
            n.right = self._ins(n.right, k, v)
        else:
            n.value = v
            return n

        _upd(n)
        b = _bf(n)

        # Left Left
        if b > 1 and k < (n.left.key if n.left else k):
            return _rot_r(n)
        # Right Right
        if b < -1 and k > (n.right.key if n.right else k):
            return _rot_l(n)
        # Left Right
        if b > 1 and k > (n.left.key if n.left else k):
            n.left = _rot_l(n.left)  # type: ignore[arg-type]
            return _rot_r(n)
        # Right Left
        if b < -1 and k < (n.right.key if n.right else k):
            n.right = _rot_r(n.right)  # type: ignore[arg-type]
            return _rot_l(n)

        return n


# ---------------------------
# Benchmark + tests
# ---------------------------

def gen_keys(n: int, mode: str, seed: int) -> List[int]:
    rnd = random.Random(seed)
    if mode == "dense":
        arr = list(range(n))
        rnd.shuffle(arr)
        return arr
    # sparse: random u64
    s = set()
    while len(s) < n:
        s.add(rnd.getrandbits(64))
    return list(s)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200_000)
    ap.add_argument("--lookups", type=int, default=200_000)
    ap.add_argument("--mode", choices=["dense", "sparse"], default="dense")
    ap.add_argument("--seed", type=int, default=123)
    args = ap.parse_args()

    keys = gen_keys(args.n, args.mode, args.seed)
    lookup_keys = keys[:]
    random.Random(args.seed + 1).shuffle(lookup_keys)
    lookup_keys = lookup_keys[: args.lookups]

    art = ARTMap()
    avl = AVLMap()
    ref = {}

    # --- Insert benchmark
    t0 = time.perf_counter()
    for k in keys:
        art.insert(u64_to_art_key(k), k)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    for k in keys:
        avl.insert(k, k)
    t3 = time.perf_counter()

    t4 = time.perf_counter()
    for k in keys:
        ref[k] = k
    t5 = time.perf_counter()

    # --- Correctness quick check
    for k in lookup_keys[: min(10_000, len(lookup_keys))]:
        v1 = art.get(u64_to_art_key(k))
        v2 = avl.get(k)
        v3 = ref.get(k)
        if v1 != v3 or v2 != v3:
            raise AssertionError(f"Mismatch for {k}: ART={v1}, AVL={v2}, dict={v3}")

    # --- Lookup benchmark
    t6 = time.perf_counter()
    s_art = 0
    for k in lookup_keys:
        s_art ^= (art.get(u64_to_art_key(k)) or 0)
    t7 = time.perf_counter()

    t8 = time.perf_counter()
    s_avl = 0
    for k in lookup_keys:
        s_avl ^= (avl.get(k) or 0)
    t9 = time.perf_counter()

    t10 = time.perf_counter()
    s_ref = 0
    for k in lookup_keys:
        s_ref ^= (ref.get(k) or 0)
    t11 = time.perf_counter()

    assert s_art == s_ref == s_avl

    print(f"Mode: {args.mode}, n={args.n}, lookups={args.lookups}")
    print(f"Insert  ART: {t1-t0:.4f}s")
    print(f"Insert  AVL: {t3-t2:.4f}s")
    print(f"Insert dict: {t5-t4:.4f}s")
    print(f"Lookup  ART: {t7-t6:.4f}s")
    print(f"Lookup  AVL: {t9-t8:.4f}s")
    print(f"Lookup dict: {t11-t10:.4f}s")

if __name__ == "__main__":
    main()
