func runningSum(nums []int) []int {
    answer  := make([]int, 0);
    answer = append(answer, nums[0]);
    
    for i:=1; i < len(nums); i++ {
        answer = append(answer, nums[i] + answer[len(answer) - 1]);
    }
    
    return answer;
}