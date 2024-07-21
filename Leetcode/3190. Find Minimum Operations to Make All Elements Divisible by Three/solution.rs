impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut operations = 0;
        
        for num in &nums {
            if *num % 3 != 0 {
                operations += 1;
            }
        }

        operations
    }
}