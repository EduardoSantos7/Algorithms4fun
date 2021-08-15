impl Solution {
    pub fn three_sum_closest(mut nums: Vec<i32>, target: i32) -> i32 {
        let mut min_dif = i32::MAX;
        let n = nums.len() - 1;
        let mut res = -1;
        
        nums.sort();
        
        for i in 0..nums.len() - 2 {
            
            if i != 0 && nums[i] == nums[i-1] {continue}
            
            let (mut l, mut r) = (i + 1, n);
            while l < r {
                let sum = nums[i] + nums[l] + nums[r];
                let dif = (sum - target).abs();
                
                if dif < min_dif {
                    min_dif = dif;
                    res = sum;
                }
                
                if sum == target {
                    return sum
                }
                
                if sum < target {
                    l += 1;
                } else {
                    r -= 1;
                }
            } 
        }
        res
    }
}