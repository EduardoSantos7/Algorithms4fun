use std::collections::HashSet;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut solo = HashSet::new();
        let mut pairs = 0;

        for char in s.chars() {
            if solo.contains(&char) {
                pairs += 1;
                solo.remove(&char);
            } else {
                solo.insert(char);
            }
        }

        pairs * 2 + (if solo.len() > 0 { 1 } else { 0 })
    }
}
