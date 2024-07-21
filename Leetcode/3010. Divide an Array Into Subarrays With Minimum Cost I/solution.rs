impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        let min1 = nums[0];
        let mut min2 = nums[1];
        let mut min3 = nums[2];

        for i in 2..nums.len() {
            if min2 > nums[i] {
                min3 = min2;
                min2 = nums[i];
            }
            else if min3 > nums[i] {
                min3 = nums[i];
            }
        }

        return min1 + min2 + min3
    }
}