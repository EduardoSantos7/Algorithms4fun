use std::cmp;

impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut max = 0;
        for (i, num) in arr.iter().enumerate() {
            max = cmp::max(max, *num);
            if max == i as i32 {
                ans += 1;
            }
        }
        ans
    }
}
