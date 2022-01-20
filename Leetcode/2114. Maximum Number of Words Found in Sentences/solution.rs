use std::cmp;


impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        let mut max_len = 0;
        
        for sentence in sentences.iter() {
            max_len = cmp::max(max_len, sentence.split(' ').count());
        }
        
        max_len as i32
    }
}