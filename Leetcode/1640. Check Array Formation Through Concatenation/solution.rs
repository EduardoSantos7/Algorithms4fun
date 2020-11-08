use std::collections::HashMap;

impl Solution {
    pub fn can_form_array(arr: Vec<i32>, pieces: Vec<Vec<i32>>) -> bool {
        let mut index = HashMap::new();

        for elem in pieces {
            index.insert(elem[0], elem);
        }

        let mut result = Vec::new();

        for elem in &arr {
            match index.get(&elem) {
                Some(list) => {
                    for num in list {
                        result.push(*num);
                    }
                }
                None => continue,
            }
        }

        return result == arr;
    }
}
