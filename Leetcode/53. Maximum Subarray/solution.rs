use std::cmp::max;

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut maxes = nums[0];
        let mut ans = nums[0];

        for i in 1..nums.len() {
            maxes = max(maxes + nums[i], nums[i]);
            ans = max(maxes, ans);
        }

        ans
    }
}
