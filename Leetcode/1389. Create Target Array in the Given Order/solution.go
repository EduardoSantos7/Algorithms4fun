func createTargetArray(nums []int, index []int) []int {
	result := []int{}
	for i := 0; i < len(index); i++ {
		result = append(result, 0)                   // Just create an extra spot
		copy(result[index[i]+1:], result[index[i]:]) // Shift
		result[index[i]] = nums[i]                   // Asign
	}
	return result
}
