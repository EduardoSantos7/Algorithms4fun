impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        let mut result = false;

        while i < bits.len() {
            if bits[i] == 0 {
                i += 1;
                result = true;
                continue;
            }

            i += 2;
            result = false;
        }

        result
    }
}