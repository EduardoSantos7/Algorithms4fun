impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec: : new()

        for c in s.chars() {
            if c == '(' | | c == '{' | | c == '[' {
                stack.push(c)
            }
            else {
                let last = stack.pop()

                if last.is_none() == true {
                    return false
                }

                if c == '}' & & last != Some('{'){
                    return false
                }

                else if c == ')' & & last != Some('('){
                    return false
                }

                else if c == ']' & & last != Some('['){
                    return false
                }
            }
        }

        stack.is_empty()
    }
}
