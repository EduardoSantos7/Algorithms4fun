impl Solution {
    pub fn count_letters(s: String) -> i32 {
        let mut total = 1;
        let mut count = 1;
        for i in 1..s.len() {
            if s.chars().nth(i) == s.chars().nth(i - 1) {
                count += 1;
            }
            else {
                count = 1;
            }
            total += count;
        }
        total
    }
}