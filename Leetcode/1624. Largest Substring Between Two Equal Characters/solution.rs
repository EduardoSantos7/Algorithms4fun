use std::cmp;
use std::collections::HashMap;

impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        let mut mem = HashMap::new();
        let mut max_substring_len: i32 = 0;
        let mut possible_substring = false;

        for (i, chr) in s.chars().enumerate() {
            if let Some(char_mem) = mem.get(&chr) {
                possible_substring = true;
                max_substring_len = cmp::max(max_substring_len, (i as i32) - char_mem - 1) as i32;
            } else {
                mem.insert(chr, (i as i32));
            }
        }

        if possible_substring {
            return max_substring_len;
        }

        -1
    }
}
