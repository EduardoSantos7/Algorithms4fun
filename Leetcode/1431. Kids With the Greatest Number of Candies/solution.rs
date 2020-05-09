impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {

        let mut result: Vec<bool> = Vec::new();
        let cur_max = Solution::max(&candies);

        for num in candies.iter() {
            if (num + extra_candies) >= cur_max{
                result.push(true);
            }
            else{
                result.push(false);
            }
        }
        result
    }
    
    pub fn max(list: &Vec<i32>) -> i32 {
        let mut cur_max: i32 = 0; // Nobody can have less than 1 candy
        for num in list.iter() {
            if num > &cur_max {
                cur_max = *num;
            }
        }
        cur_max
    }
}