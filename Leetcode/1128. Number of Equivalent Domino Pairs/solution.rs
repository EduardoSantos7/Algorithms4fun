use std::collections::HashMap;

impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let mut cache: HashMap<(i32, i32), i32> = HashMap::new();
        for domino in &dominoes {
            let (a, b) = (domino[0], domino[1]);
            let pair = if a < b { (a, b) } else { (b, a) };
            *cache.entry(pair).or_insert(0) += 1 ;
        }

        cache.values().map(|&value| value * (value - 1) / 2).sum()
    }
}