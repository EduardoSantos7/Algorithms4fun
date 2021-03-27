impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        if n < 3 {
            return 0;
        } else if n == 2 {
            return 1;
        }

        let n = n as usize;

        let mut nums: Vec<bool> = vec![false; n];
        let mut primes = 1;

        for i in (3..n).step_by(2) {
            if !nums[i] {
                primes += 1;
                for c in (i * i..n).step_by(i + i) {
                    nums[c] = true;
                }
            }
        }
        primes
    }
}
