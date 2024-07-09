impl Solution {
    pub fn find_non_min_or_max(mut nums: Vec<i32>) -> i32 {
        if nums.len() <= 2 {
            return -1
        }

        let mut min = nums[0];
        let mut max = nums[0];
        for &num in &nums {
            min = min.min(num);
            max = max.max(num);
        }

        for &num in &nums {
            if num != max && num != min{
                return num
            }
        }

        -1
    }
}