func maxProduct(nums []int) int {
	val_1, val_2 := 0, 0

	for _, num := range nums {
		if num > val_1 {
			val_2 = val_1
			val_1 = num
		} else if num > val_2 {
			val_2 = num
		}
	}

	return (val_1 - 1) * (val_2 - 1)
}