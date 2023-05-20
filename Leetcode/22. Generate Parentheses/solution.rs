impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        if n == 0 {
            return vec!["".to_string()];
        }

        let mut answer: Vec<String> = Vec::new();
        for left_count in 0..n {
            for left_string in Solution::generate_parenthesis(left_count) {
                for right_string in Solution::generate_parenthesis(n - left_count - 1) {
                    answer.push(format!("({}){}", left_string, right_string));
                }
            }
        }

        answer
    }
}