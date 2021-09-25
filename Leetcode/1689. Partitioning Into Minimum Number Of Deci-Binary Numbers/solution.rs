impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        let mut max = '0' as u32;
        
        for character in n.chars() {
            if character as u32 > max {
                max = character as u32
            }
        }
        
        (max - '0' as u32) as i32
    }
}