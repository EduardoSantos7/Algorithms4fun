impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        let mut counter = 0;
        let mut mem = vec![true; n as usize];

        for num in 2..n {
            let index = num as usize;
            if mem[index] {
                counter += 1;
                for i in (num..n).step_by(index) {
                    mem[i as usize] = false
                }
            }
        }

        counter
    }
}
