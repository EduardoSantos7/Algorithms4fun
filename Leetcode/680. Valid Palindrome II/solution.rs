impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let mut i = 0 as usize;
        let mut j = s.len() - 1;
        let chars: &[u8] = s.as_bytes();
        while i <= j {
            if chars[i] != chars[j] {
                i += 1;
                j -= 1;
                continue;
            }
            return Solution::is_palindrome(&chars, i + 1, j) || Solution::is_palindrome(&chars, i, j - 1);
        }
        true
    }

    pub fn is_palindrome(chars: &[u8], i: usize, j: usize) -> bool {
        let (mut i, mut j) = (i, j);
        while i <= j {
            if chars[i] != chars[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        true
    }
}