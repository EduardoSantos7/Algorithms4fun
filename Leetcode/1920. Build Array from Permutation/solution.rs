impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        
        for i in 0..nums.len() {
            ans.push(nums[nums[i as usize] as usize]);
        }
        
        ans
    }
}