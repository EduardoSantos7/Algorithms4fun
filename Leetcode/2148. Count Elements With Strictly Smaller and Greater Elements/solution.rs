impl Solution {
    pub fn count_elements(mut nums: Vec<i32>) -> i32 {
        let mut N = nums.len();
        if N < 3 { return 0 }
        let mut res = 0;
        nums.sort();

        for i in 1..N-1 {
            if (nums[0] < nums[i] && nums[i] < nums[N - 1]) { res += 1; }
        }

        res
    }
}