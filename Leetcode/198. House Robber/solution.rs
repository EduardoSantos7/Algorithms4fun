impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let (mut a, mut b, mut temp) = (0, 0, 0);

        for num in &nums {
            temp = if num + a > b { num + a } else { b };
            a = b;
            b = temp;
        }
        b
    }
}
