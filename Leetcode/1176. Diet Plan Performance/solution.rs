impl Solution {
    pub fn diet_plan_performance(calories: Vec<i32>, k: i32, lower: i32, upper: i32) -> i32 {
        let k = k as usize;
        let mut points = 0;

        // Calculate the sum of the first window
        let mut window_sum: i32 = calories.iter().take(k).sum();

        // Evaluate the first window
        points += match window_sum {
            s if s < lower => -1,
            s if s > upper => 1,
            _ => 0,
        };

        // Slide the window
        for i in k..calories.len() {
            window_sum += calories[i] - calories[i - k];
            points += match window_sum {
                s if s < lower => -1,
                s if s > upper => 1,
                _ => 0,
            };
        }

        points
    }
}
