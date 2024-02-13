use std::collections::HashSet;

impl Solution {
    pub fn count_distinct_integers(nums: Vec<i32>) -> i32 {
        let mut distinct_nums = HashSet::new();
        for &num in &nums {
            distinct_nums.insert(num);
            distinct_nums.insert(num.to_string().chars().rev().collect::<String>().parse().unwrap());
        }
        distinct_nums.len() as i32
    }
}