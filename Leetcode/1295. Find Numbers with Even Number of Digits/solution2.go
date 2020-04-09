func findNumbers(nums []int) int {
	result := 0
	seen := map[int]int{}
	for i := 0; i < len(nums); i++ {
		if val, ok := seen[nums[i]]; ok {
			if val%2 == 0 {
				result++
			}
			continue
		}
		count := 0
		for nums[i] > 0 {
			nums[i] /= 10
			count += 1
		}
		seen[nums[i]] = count
		if count%2 == 0 {
			result += 1
		}
	}
	return result
}
