impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let mut delete = 0;
        for col in 0..strs[0].len() {
            for row in 1..strs.len() {
                if !(strs[row-1].as_bytes()[col] <= strs[row].as_bytes()[col]) {
                    delete += 1;
                    break;
                }
            }
        }
        delete
    }
}