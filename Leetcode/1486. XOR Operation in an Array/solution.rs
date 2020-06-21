impl Solution {
    pub fn xor_operation(n: i32, start: i32) -> i32 {
        let mut xor = start;
        for i in 1..n {
            xor ^= start + 2*i
        }
        xor
    }
}