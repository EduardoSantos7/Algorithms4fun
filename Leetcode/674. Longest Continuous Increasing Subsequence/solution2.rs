impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        let mut max = 0;
        let mut past = 0;
        
        for i in 0..nums.len() {
            // Check if it's a increasing sequence
            if i > 0 && nums[i-1] >= nums[i] {
                past = i as i32;
            }
            max = if (i as i32 - past + 1) > max { (i as i32 - past + 1)} else { max };
        }
        
        max
    }
}