use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut count = HashMap::new();

        for chr in s.chars() {
            *count.entry(chr).or_insert(0) += 1;
        }

        for (i, chr) in s.chars().enumerate() {
            if count.get(&chr) == Some(&1) {
                return i as i32;
            }
        }

        -1
    }
}
