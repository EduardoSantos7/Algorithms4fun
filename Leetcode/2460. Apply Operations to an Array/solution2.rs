impl Solution {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut next: usize;
        let mut nums_shifted: Vec<i32> = Vec::new();

        for i in 0..n {
            next = i + 1;
            if next < n && nums[i] == nums[next] {
                nums[i] += nums[i];
                nums[next] = 0;
            }
            if nums[i] != 0 {
                nums_shifted.push(nums[i]);
            }
        }

        nums_shifted.resize(n, 0);
        nums_shifted
    }
}
