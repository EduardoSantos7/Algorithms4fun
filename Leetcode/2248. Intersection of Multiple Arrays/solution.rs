use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result: HashSet<i32> = nums[0].iter().copied().collect();
        for array in &nums[1..] {
            result.retain(|&x| array.contains(&x));
        }

        let mut result_vec: Vec<i32> = result.into_iter().collect();
        result_vec.sort();
        result_vec
    }
}
