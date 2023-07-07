func findMaxAverage(nums []int, k int) float64 {
    var start, count int = 0, 0;
    var max_avg, avg float64 = 0.0, 0.0;

    for i := start; i < k; i++ {
        count += nums[i]
    }
    
    max_avg = float64(count) / float64(k)
    avg = max_avg

    for i := k; i < len(nums); i++ {
        count += nums[i] - nums[start]
        start +=  1;
        avg = float64(count) / float64(k);
        if avg > max_avg {
            max_avg = avg;
        }
    }

    return max_avg;
}