impl Solution {
    pub fn trim_mean(mut arr: Vec<i32>) -> f64 {
        arr.sort();
        let five_percent = (arr.len() as f64 * 0.05) as usize; // Use f64 and usize for indices calculation
        let sum: i32 = arr[five_percent..(arr.len() - five_percent)] // Correct slicing to exclude bounds
                         .iter()    // Use iter() to get iterator over &i32
                         .sum();    // Sum the i32 values directly
        let count = arr.len() - 2 * five_percent; // Calculate the number of elements considered in the sum
        sum as f64 / count as f64 // Convert sum and count to f64 for division to return f64
    }
}
