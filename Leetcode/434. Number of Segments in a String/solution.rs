impl Solution {
    pub fn count_segments(s: String) -> i32 {
        let mut segments = 0;

        for i in 0..s.len() {
            if ((i == 0 || s.chars().nth(i-1) == Some(' ')) && (s.chars().nth(i) != Some(' '))) {
                segments += 1;
            } 
        }

        return segments;
    }
}