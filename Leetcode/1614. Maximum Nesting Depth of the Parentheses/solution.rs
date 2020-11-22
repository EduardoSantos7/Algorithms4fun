use std::cmp;

impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut parentheses_counter = 0;
        let mut max_depth = 0;
        
        for c in s.chars() {
            if c == '(' {
                parentheses_counter += 1;
                max_depth = cmp::max(max_depth, parentheses_counter);
            } else if c == ')'{
                parentheses_counter -= 1;
            }
        }
        
        max_depth
    }
}
