func findNumbers(nums []int) int {
	result := 0
	for i := 0; i < len(nums); i++ {
		count := 0
		for nums[i] > 0 {
			nums[i] /= 10
			count += 1
		}
		if count%2 == 0 {
			result += 1
		}
	}
	return result
}
