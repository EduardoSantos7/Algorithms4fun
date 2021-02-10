use std::collections::HashMap;

impl Solution {
    pub fn can_be_equal(target: Vec<i32>, arr: Vec<i32>) -> bool {
        let mut count = HashMap::new();

        for i in 0..target.len() {
            *count.entry(target[i]).or_insert(0) += 1;
            *count.entry(arr[i]).or_insert(0) -= 1;
        }

        for val in count.values() {
            if *val != 0 {
                return false;
            }
        }

        true
    }
}
