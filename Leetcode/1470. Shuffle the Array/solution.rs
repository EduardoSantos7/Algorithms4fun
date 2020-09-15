impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut vec: Vec<i32> = Vec::with_capacity(2 * n as usize);
        for i in 0..n {
            vec.push(nums[i as usize]);
            vec.push(nums[(i + n) as usize])
        }
        vec
    }
}
