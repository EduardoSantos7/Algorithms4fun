impl Solution {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut next: usize;
        for i in 0..n-1 {
            next = i + 1;
            if nums[i] == nums[next] {
                nums[i] += nums[i];
                nums[next] = 0;
            }
        }
        
        nums.sort_by_key(|&x| if x == 0 { 1 } else { 0 });
        
        nums
    }
}