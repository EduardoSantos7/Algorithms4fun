impl Solution {
    pub fn largest_perimeter(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable_by_key(|n| -n);
        nums.windows(3).find(|n| n[0] < n[1] + n[2]).map(|n| n[0] + n[1] + n[2]).unwrap_or(0)
    }
}