package main

func MoveElementToEnd(array []int, toMove int) []int {
	keep := 0

	for runner := 0; runner < len(array); runner += 1 {
		if array[runner] == toMove {
			continue
		}
		// Swap
		temp := array[keep]
		array[keep] = array[runner]
		array[runner] = temp
		keep += 1
	}
	return array
}
