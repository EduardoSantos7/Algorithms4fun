impl Solution {
    pub fn arrange_coins(mut n: i32) -> i32 {
        let mut left = 0 as i64;
        let mut right = n as i64;

        while left <= right {
            let mid: i64 = (right + left) / 2;
            let curr: i64 = mid * (mid + 1) / 2;

            if curr == n as i64 {
                return mid as i32;
            }
            if (n as i64) < curr {
                right = mid - 1;
            } else {
                left = mid + 1
            }
        }

        right as i32
    }
}
