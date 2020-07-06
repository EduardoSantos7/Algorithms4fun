package main

func BinarySearch(array []int, target int) int {
	return BinarySearchHelper(array, target, 0, len(array)-1)
}

func BinarySearchHelper(array []int, target int, left int, right int) int {
	if right < left {
		return -1
	}

	mid := int((left + right) / 2)

	if array[mid] == target {
		return mid
	} else if array[mid] > target {
		return BinarySearchHelper(array, target, left, mid-1)
	} else {
		return BinarySearchHelper(array, target, mid+1, right)
	}
}
