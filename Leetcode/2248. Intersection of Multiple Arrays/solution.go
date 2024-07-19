import (
	"sort"
)

func intersection(nums [][]int) []int {
	result := make([]int, len(nums[0]))
	copy(result, nums[0])

	for _, arr := range nums[1:] {
		result = intersect(result, arr)
	}

	sort.Ints(result)
	return result
}

func intersect(arr1 []int, arr2 []int) []int {
	set := make(map[int]bool)
	result := []int{}

	for _, num := range arr1 {
		set[num] = true
	}

	for _, num := range arr2 {
		if set[num] {
			result = append(result, num)
		}
	}

	return result
}