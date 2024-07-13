impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool
    {
        // Create a hash set to check for all expected elements
        let expected_elements: std::collections::HashSet<_> = arr.iter().collect();
        if expected_elements.len() == 1 { return true; } else if expected_elements.len() != arr.len() { return false; }
        // Initialize min and second_min either to maximum possible i32 values
        let (mut min, mut second_min) = (i32::MAX, i32::MAX);

        // Find the two smallest unique elements
        for &value in &arr {
            if value < min {
                second_min = min;
                min = value;
            } else if value < second_min && value != min {
                second_min = value;
            }
        }

        // If we cannot find a distinct second minimum, it's not a valid AP
        // if second_min == i32::MAX {
        //     return false;
        // }

        let common_diff = second_min - min;

        // Check if every expected value based on the common difference is present
        for i in 0..arr.len() {
            let expected_value = min + i as i32 * common_diff;
            if !expected_elements.contains(&expected_value) {
                return false;
            }
        }

        true
    }
}