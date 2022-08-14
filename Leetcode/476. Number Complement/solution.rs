impl Solution {
    pub fn find_complement(num: i32) -> i32 {
        let mut mask = 1;
        // create a mask of n bit where n is the same size of num
        while mask < num {
            mask <<= 1;
            mask += 1;
        }
        // xor of a num with a mask of only 1s is equivalent to complement
        return num ^ mask
    }
}