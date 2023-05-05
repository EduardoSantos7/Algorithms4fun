use std::collections::HashSet;

impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let vowels: HashSet<char> = ['a', 'e', 'i', 'o', 'u'].iter().cloned().collect();

        let s_chars: Vec<char> = s.chars().collect();
        let mut count = 0;
        for i in 0..k {
            if vowels.contains(&s_chars[i as usize]) {
                count += 1;
            }
        }
        let mut answer = count;

        for i in (k as usize)..s.len() {
            count += vowels.contains(&s_chars[i]) as i32;
            count -= vowels.contains(&s_chars[i - k as usize]) as i32;
            if count > answer {
                answer = count;
            }
        }

        return answer;
    }
}