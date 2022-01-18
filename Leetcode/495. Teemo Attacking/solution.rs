impl Solution {
    pub fn find_poisoned_duration(time_series: Vec<i32>, duration: i32) -> i32 {
        let mut time_poisoned = duration;
        
        for i in 1..time_series.len() {
            let diff = time_series[i] - time_series[i-1];
            time_poisoned += if diff > duration { duration } else { diff };
        }
        
        time_poisoned
    }
}