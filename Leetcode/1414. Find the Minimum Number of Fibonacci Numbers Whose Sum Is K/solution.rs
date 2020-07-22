impl Solution {
    pub fn find_min_fibonacci_numbers(k: i32) -> i32 {
        let mut fibs = Vec::new();
        let mut count = 0;
        let mut res = 0;
        
        fibs.push(1);
        fibs.push(1);
        
        while fibs[fibs.len() - 1] < k {
            fibs.push(fibs[fibs.len() - 1] + fibs[fibs.len() - 2]);
        }

        for num in fibs.iter().rev() {
            if num + count < k {
                count += num;
                res += 1;
            }
            else if num + count == k {
                res += 1;
                break
            }
        }
        res
    }
}