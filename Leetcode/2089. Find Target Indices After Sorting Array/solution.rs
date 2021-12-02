impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut smaller_than_target_count = 0;
        let mut target_count = 0;

        for num in nums.iter() {
            if *num < target {
                smaller_than_target_count += 1;
            }
            if *num == target {
                target_count += 1;
            }
        }

        (smaller_than_target_count..smaller_than_target_count + target_count).collect()
    }
}
