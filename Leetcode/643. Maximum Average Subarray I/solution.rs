impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let k = k as usize;
        let mut count: i32 = nums.iter().take(k).sum();
        let mut max_count = count;

        for i in k..nums.len() {
            count += nums[i] - nums[i - k];
            if count > max_count {
                max_count = count;
            }
        }

        max_count as f64 / k as f64
    }
}