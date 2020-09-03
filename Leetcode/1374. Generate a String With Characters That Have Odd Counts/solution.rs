impl Solution {
    pub fn generate_the_string(n: i32) -> String {
        let mut v: Vec<char> = Vec::new();
        
        if n % 2 == 1 {
            for i in 0..n {
                v.push('a');
            }
        }
        else {
            for i in 0..n - 1 {
                v.push('a');
            }
            v.push('b');
        }
        
        v.into_iter().collect()
    }
}