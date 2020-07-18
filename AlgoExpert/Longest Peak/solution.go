package main

import "math"

func LongestPeak(array []int) int {
	max_len := 0

	for i := 1; i < len(array)-1; i++ {
		is_peak := array[i-1] < array[i] && array[i] > array[i+1]

		if !is_peak {
			continue
		}

		left := i - 2
		right := i + 2

		for left >= 0 && array[left] < array[left+1] {
			left -= 1
		}

		for right < len(array) && array[right] < array[right-1] {
			right += 1
		}

		max_len = int(math.Max(float64(max_len), float64(right-left-1)))

	}
	return max_len
}
