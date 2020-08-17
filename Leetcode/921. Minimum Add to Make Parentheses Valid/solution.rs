impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut stack = Vec::new();

        for c in s.chars() {
            if stack.len() > 0 && stack[stack.len() - 1] == '(' && c == ')' {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        stack.len() as i32
    }
}
