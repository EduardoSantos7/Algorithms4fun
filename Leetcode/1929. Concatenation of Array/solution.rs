impl Solution {
    pub fn get_concatenation(mut nums: Vec<i32>) -> Vec<i32> {
        for i in 0..nums.len() {
            nums.push(nums[i]);
        }
        
        nums
    }
}