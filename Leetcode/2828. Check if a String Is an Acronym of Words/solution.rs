impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        words.iter().map(|word| word.chars().next().unwrap()).collect::<String>() == s
    }
}