func sumIndicesWithKSetBits(nums []int, k int) (result int) {
	if k == 0 {
		return nums[0]
	}

	if len(nums) == 1 {
		return 0
	}

	index := 1
	for i := 1; i < k; i++ {
		index = (index << 1) | 1
	}

	for ; index < len(nums); index++ {
		if index&1 == 0 || countBits(index) != k {
			continue
		}

		for i := index; i < len(nums); i <<= 1 {
			result += nums[i]
		}
	}

	return result
}

func countBits(x int) (result int) {
	for ; x > 0; x >>= 1 {
		result += x & 1
	}

	return result
}