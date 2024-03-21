impl Solution {
    pub fn sum_indices_with_k_set_bits(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as u32;
        (0..nums.len()).fold(0, |acc, i| if i.count_ones() == k { acc + nums[i] } else { acc })
    }
}