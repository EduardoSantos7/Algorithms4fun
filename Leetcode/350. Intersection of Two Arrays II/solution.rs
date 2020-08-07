use std::collections::HashMap;

impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut mem = HashMap::new(); 
        let mut answer = vec![];
        
        for num in nums1 {
            *mem.entry(num).or_insert(0) += 1;
        }
        
        for num in nums2 {
            if mem.contains_key(&num) && mem[&num] > 0 {
                answer.push(num);
                mem.insert(num, mem[&num] - 1);
            }
        }
        
        answer
    }
}
