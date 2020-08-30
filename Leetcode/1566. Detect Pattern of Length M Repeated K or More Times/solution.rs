impl Solution {
    pub fn contains_pattern(arr: Vec<i32>, m: i32, k: i32) -> bool {
        let (mut i, mut j, mut count, mut n) = (0, m, 0, arr.len() as i32);

        while j < n {
            if arr[i as usize] != arr[j as usize] {
                count = 0;
            } else {
                count += 1;
                if (count) >= (k - 1) * m {
                    return true;
                }
            }
            i += 1;
            j += 1;
        }

        false
    }
}
