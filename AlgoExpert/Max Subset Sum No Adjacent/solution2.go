package main

func MaxSubsetSumNoAdjacent(array []int) int {
	if len(array) == 0 {
		return 0
	}
	if len(array) == 1 {
		return 1
	}

	first, second := Max(array[0], array[1]), array[0]

	for index := 2; index < len(array); index++ {
		temp := Max(first, array[index]+second)
		second = first
		first = temp
	}

	return first
}

func Max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
