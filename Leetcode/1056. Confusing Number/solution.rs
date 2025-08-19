use std::collections::HashMap;

impl Solution {
    pub fn confusing_number(n: i32) -> bool {
        let str_n = n.to_string();
        let num_map: HashMap<char, char> = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')].iter().cloned().collect();
        let rotated: Option<String> = str_n.chars().rev().map(|ch| num_map.get(&ch).copied()).collect();

        // If any digit invalid, rotated will be None, return false
        if rotated.is_none() {
            return false;
        }

        let rotated = rotated.unwrap();

        rotated!= str_n
    }
}