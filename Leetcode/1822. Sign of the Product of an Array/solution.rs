impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut count_negative_numbers = 0;

        for num in nums {
            if num < 0 {
                count_negative_numbers += 1;
                continue;
            }
            if num == 0{
                return 0
            }
        }

        return if count_negative_numbers % 2 == 0 {1} else {-1}
    }
}