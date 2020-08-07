impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut counter = nums[0];
        let mut answer = vec![counter];
        
        for i in 1..nums.len() {
            counter += nums[i];
            answer.push(counter);
        }
        
        answer
    }
}