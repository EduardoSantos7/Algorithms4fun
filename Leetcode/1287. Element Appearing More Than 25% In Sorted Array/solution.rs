use std::collections::HashMap;

impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let mut mem = HashMap::new();
        // let mut count = 0;
        
        for num in &arr {
            let count = match mem.get(&num) {
                Some(x) => x + 1,
                None => 1,
            };
            mem.insert(num, count);
        }
        
        let mut res = 0;
        for (&key, &rep) in mem.iter() {
            if (rep as f32 / arr.len() as f32) as f32 > 0.25 {
                res = *key;
                break;
            }
        }
        
        return res
    }
}