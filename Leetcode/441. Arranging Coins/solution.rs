impl Solution {
    pub fn arrange_coins(mut n: i32) -> i32 {
        let mut complete_rows = 0;
        for i in 0..n {
            n -= i + 1;
            if n >= 0 {
                complete_rows += 1;
                continue;
            }
            break;
        }
        complete_rows
    }
}
