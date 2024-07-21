func minimumOperations(nums []int) int {
	operations := 0
	for _, num := range nums {
		if num%3 == 0 {
			continue
		}
		operations += 1
	}
	return operations
}