impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut val_1 = 0;
        let mut val_2 = 0;
        
        for num in nums {
            if num > val_1 {
                val_2 = val_1;
                val_1 = num;
            }
            else if num > val_2{
                val_2 = num;
            }
        }
        return (val_1 - 1) * (val_2 - 1)
    }
}