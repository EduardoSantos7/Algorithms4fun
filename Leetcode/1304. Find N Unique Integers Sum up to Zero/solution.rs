impl Solution {
    pub fn sum_zero(n: i32) -> Vec<i32> {
        let rem = n % 2;
        let loops = n /2 + 1;
        let mut res: Vec<i32> = Vec::new();
        
        if rem == 1 {
            res.push(0);
        }
        
        for i in 1..loops {
            res.push(i);
            res.push(-i);
        }
        
        res
    }
}