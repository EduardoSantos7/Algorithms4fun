impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut splitted_words = s.split_whitespace();
        let mut reversed_words: Vec<String> = Vec::new();
        
        for word in splitted_words {
            reversed_words.push(word.chars().rev().collect());
        }
        
        reversed_words.join(" ")
    }
}