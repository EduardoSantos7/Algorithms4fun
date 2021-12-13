impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        let mut lower: i64 = 1;
        let mut higher: i64 = num as i64;
        
        while lower <= higher {
            let mut mid: i64 = (lower + (higher - lower) / 2) as i64;
            let square: i64 = mid * mid;

            if square == num as i64 {
                return true;
            }
            else if square > num as i64 {
                higher = mid - 1;
            }
            else {
                lower = mid + 1;
            }
        }
        
        false
    }
}