use std::collections::HashSet;
use std::hash::{Hash, Hasher};

#[derive(Debug, Clone, Copy)]
struct ApproximateFloat(f64);

impl PartialEq for ApproximateFloat {
    fn eq(&self, other: &Self) -> bool {
        (self.0 - other.0).abs() < 0.00001 // Define your tolerance level
    }
}

impl Eq for ApproximateFloat {}

impl Hash for ApproximateFloat {
    fn hash<H: Hasher>(&self, state: &mut H) {
        ((self.0 * 100000.0).round() as i64).hash(state) // Scale and round the float before hashing
    }
}

impl Solution {
    pub fn distinct_averages(mut nums: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = nums.len() - 1;
        let mut averages_seen: HashSet<ApproximateFloat> = HashSet::new();
        nums.sort();
        while i < j {
            let average = ApproximateFloat(((nums[i] as f64 + nums[j] as f64) / 2.0));
            if !averages_seen.contains(&average) {
                averages_seen.insert(average);
            }
            i += 1;
            j -= 1;
        }
        return averages_seen.len() as i32;
    }
}
