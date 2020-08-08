impl Solution {
    pub fn min_cost_to_move_chips(chips: Vec<i32>) -> i32 {
        let mut even = 0;
        for chip in &chips {
            if chip % 2 == 0 {
                even += 1;
            }
        }
        let mut min = (chips.len() as i32) - even;
        
        if even < min {
            return even;
        }
        
        min
    }
}