impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut sorted = heights.clone();
        let mut count = 0;
        sorted.sort_unstable();

        for i in 0..heights.len() {
            if heights[i] != sorted[i] {
                count += 1
            }
        }

        return count;
    }
}
