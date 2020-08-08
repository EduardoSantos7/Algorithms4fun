use std::collections::HashMap;

impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut seen = HashMap::new();
        let mut pairs = 0;
        for num in nums {
            let mut count = seen.get(&num);
            
            let freq = match count {
                Some(num) => *num,
                None => 0,
            };
            
            if freq > 0 {
                pairs += freq;
            }
            seen.insert(num, freq + 1);
        }
        pairs
    }
}
