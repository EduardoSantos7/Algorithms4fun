use std::cmp;

impl Solution {
    pub fn check_zero_ones(s: String) -> bool {
        let mut max_zero = 0;
        let mut max_ones = 0;
        let mut temp = 0;

        for i in 0..s.len() {
            if i > 0 && i < s.len() && s.as_bytes()[i] != s.as_bytes()[i - 1] {
                temp = 0;
            }

            temp += 1;
            max_zero = if s.chars().nth(i).unwrap() == '0' {
                cmp::max(max_zero, temp)
            } else {
                max_zero
            };
            max_ones = if s.chars().nth(i).unwrap() == '1' {
                cmp::max(max_ones, temp)
            } else {
                max_ones
            };
        }

        return if max_ones > max_zero { true } else { false };
    }
}
