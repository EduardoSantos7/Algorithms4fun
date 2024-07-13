impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool
    {
        // Sort the vector
        arr.sort();

        // Calculate the common difference
        let common_diff = arr[1] - arr[0];

        // Check each pair of elements for the constant difference
        for i in 2..arr.len() {
            if arr[i] - arr[i - 1] != common_diff {
                return false;
            }
        }

        true
    }
}