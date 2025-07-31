impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let mut total_sum: i32 = nums.iter().sum();
        let mut current_sum = 0;
        let mut answer = 0;
        for i in 0..nums.len() - 1 {
            current_sum += nums[i];
            if ((total_sum - current_sum) - current_sum) % 2 == 0{
                answer += 1;
            }
        }
        answer
    }
}