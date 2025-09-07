impl Solution {
    pub fn minimum_pair_removal(mut nums: Vec<i32>) -> i32 {
        fn is_non_decreasing(nums: &Vec<i32>) -> bool {
            for i in 1..nums.len() {
                if nums[i] < nums[i - 1] {
                    return false;
                }
            }
            true
        }

        fn reduce_min_sum_pair(nums: &mut Vec<i32>) {
            let mut min_sum = i32::MAX;
            let mut min_index = 1;

            for i in 1..nums.len() {
                let sum = nums[i] + nums[i - 1];
                if sum < min_sum {
                    min_sum = sum;
                    min_index = i;
                }
            }

            nums[min_index - 1] = min_sum;
            nums.remove(min_index); // remove the right element of the merged pair
        }

        let mut operations = 0;

        while !is_non_decreasing(&nums) {
            reduce_min_sum_pair(&mut nums);
            operations += 1;
        }

        operations
    }
}