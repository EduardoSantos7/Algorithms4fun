package main

import "sort"

func ThreeNumberSum(array []int, target int) [][]int {
	result := make([][]int, 0)
	sort.Ints(array)

	for i, num := range array {
		left := i + 1
		right := len(array) - 1
		for left < right {
			current_sum := num + array[left] + array[right]
			if current_sum == target {
				triplet := []int{num, array[left], array[right]}
				result = append(result, triplet)
				left += 1
				right -= 1
			} else if current_sum < target {
				left += 1
			} else {
				right -= 1
			}
		}
	}
	return result
}
