package main

func IsValidSubsequence(array []int, sequence []int) bool {
	current_target := 0
	for _, num := range array {
		if num == sequence[current_target] {
			current_target += 1
			if current_target == len(sequence) {
				return true
			}
		}
	}
	return false
}
