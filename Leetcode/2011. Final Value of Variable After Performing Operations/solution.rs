impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut acum = 0;
        
        for op in operations.into_iter() {
            if op.contains("+") {
                acum += 1;
            }
            else {
                acum -= 1;
            }
        }
        
        acum
    }
}