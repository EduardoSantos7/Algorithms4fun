use std::collections::HashMap;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut counts = HashMap::new();
        let mut pairs = 0;
        let mut solos = 0;

        for char in s.chars() {
            if counts.contains_key(&char) {
                counts.insert(char, counts[&char] + 1);
            } else {
                counts.insert(char, 1);
            }
        }

        for count in counts.values().collect::<Vec<&i32>>() {
            pairs += 2 * (count / 2);
            solos += if count % 2 > 0 { 1 } else { 0 };
        }

        pairs + (if solos > 0 { 1 } else { 0 })
    }
}
