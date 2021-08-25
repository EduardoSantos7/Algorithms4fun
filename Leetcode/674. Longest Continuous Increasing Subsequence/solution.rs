impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        let (mut left, mut right) = (0, 0);
        let mut max = 1;
        let mut res = 1;
        
        while right < nums.len() {
            // Move right pointer forward
            right += 1;
            
            // Check if it's a increasing sequence
            if right < nums.len() && nums[right] > nums[left] {
                res += 1;
                left += 1;
            } else {
                left = right;
                max = if res > max { res } else { max };
                res = 1;
            }
        }
        
        max
    }
}