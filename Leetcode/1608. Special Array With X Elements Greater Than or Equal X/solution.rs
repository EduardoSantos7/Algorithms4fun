impl Solution {
    pub fn special_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut freq = vec![0; n+1];
        let mut numbers_bigger_equal = 0;

        for num in &nums { freq[std::cmp::min(*num as usize, n)] += 1; }

        for i in (0..n + 1).rev() {
            numbers_bigger_equal += freq[i];
            if numbers_bigger_equal == i {
                return i as i32;
            }
        }

        -1
    }
}