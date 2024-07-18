impl Solution {
    pub fn sort_even_odd(nums: Vec<i32>) -> Vec<i32> {
        let mut even_nums: Vec<i32> = nums.clone().into_iter().enumerate().filter(|&(i, _)| i % 2 == 0).map(|(_, e)| e).collect();
        let mut odd_nums: Vec<i32> = nums.into_iter().enumerate().filter(|&(i, _)| i % 2 == 1).map(|(_, e)| e).collect();
        use std::cmp;
        even_nums.sort();
        odd_nums.sort_by(|a, b| b.cmp(a));
        return {
            let mut res = vec![];
            for i in 0..odd_nums.len() {
                res.push(even_nums[i]);
                res.push(odd_nums[i]);
            }

            if even_nums.len() > odd_nums.len() {
                res.push(*even_nums.last().unwrap())
            }
            res
        };
    }
}