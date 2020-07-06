package main

func BinarySearch(array []int, target int) int {
	left := 0
	right := len(array) - 1

	for left <= right {
		mid := int(right-left)/2 + left

		if array[mid] > target {
			right = mid - 1
		} else if array[mid] < target {
			left = mid + 1
		} else {
			return mid
		}
	}
	return -1
}
