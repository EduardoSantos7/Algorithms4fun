impl Solution {
    pub fn reverse_bits(mut x: u32) -> u32 {
        let (mut ans, mut power) = (0, 31);

        while x > 0 {
            ans += (x & 1) << power;
            x >>= 1;
            power -= 1;
        }
        ans
    }
}
