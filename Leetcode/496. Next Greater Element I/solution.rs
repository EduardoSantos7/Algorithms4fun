use std::collections::HashMap;

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut positions: HashMap<i32, i32> = HashMap::new();
        
        for (i, num) in nums2.iter().enumerate() {
            positions.insert(*num, i as i32);
        }
        
        let mut ans = nums1.iter().map(|num| {
            let mut cur = *positions.get(num).unwrap();
            let mut next_greater = -1;

            while cur + 1 < nums2.len() as i32 {
                if nums2[cur as usize + 1] > *num {
                    next_greater = nums2[cur as usize + 1];
                    break;
                }
                cur += 1;
            }
            next_greater
        }).collect();
        
        ans
    }
}