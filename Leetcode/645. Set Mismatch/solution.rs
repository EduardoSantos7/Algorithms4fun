impl Solution {
    pub fn find_error_nums(mut nums: Vec<i32>) -> Vec<i32> {
        let mut dup = 0;
        let mut missing = 1;
        let mut nums2 = nums.clone();
        
        for i in 0..nums2.len() {
            let num = nums2[i].abs() as usize - 1;
            if(nums2[num] < 0) {
                dup = nums2[i].abs();
            }
            else {
                nums2[num] *= -1;
            }
        }
        
        for i in 1..nums2.len() {
            if nums2[i] > 0 {
                missing = i as i32 + 1;
            }
        }
        
        return vec![dup, missing];
    }
}