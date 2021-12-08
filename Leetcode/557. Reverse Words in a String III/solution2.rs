impl Solution {
    pub fn reverse_words(s: String) -> String {
        s.split_whitespace().map(|word| word.chars().rev().collect::<String>()).collect::<Vec<_>>().join(" ")
    }
}