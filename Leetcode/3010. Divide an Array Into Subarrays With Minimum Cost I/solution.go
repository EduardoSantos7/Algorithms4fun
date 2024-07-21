func minimumCost(nums []int) int {
	min1 := nums[0]
	min2 := nums[1]
	min3 := nums[2]

	for i := 2; i < len(nums); i++ {
		if min2 > nums[i] {
			min3 = min2
			min2 = nums[i]
		} else if min3 > nums[i] {
			min3 = nums[i]
		}
	}

	return min1 + min2 + min3
}