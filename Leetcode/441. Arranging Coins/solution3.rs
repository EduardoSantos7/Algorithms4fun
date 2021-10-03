impl Solution {
    pub fn arrange_coins(mut n: i32) -> i32 {
        return (((2 * n as i64) as f64 + 0.25).powf(0.5) - 0.5) as i32;
    }
}
