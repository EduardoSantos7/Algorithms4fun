public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
        int start = 0, count = 0;
        double max_avg = 0.0, avg = 0.0;

        for (int i = 0; i < k; i++) count += nums[i];

        max_avg = avg = (double)count / k;

        for (int i = k; i < nums.Count(); i++) {
            count += nums[i] - nums[start];
            start += 1;
            avg = (double)count / k;
            if (avg > max_avg) max_avg = avg;
        }

        return max_avg;
    }
}