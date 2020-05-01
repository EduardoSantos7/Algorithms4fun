func luckyNumbers(matrix [][]int) []int {
	s, r := make(map[int]struct{}), make([]int, 0)

	var exists = struct{}{}

	for row := 0; row < len(matrix); row++ {
		min_val := min(matrix[row])
		s[min_val] = exists
	}

	for col := 0; col < len(matrix[0]); col++ {
		current_max := -1
		for row := 0; row < len(matrix); row++ {
			num := matrix[row][col]
			if num > current_max {
				current_max = num
			}
		}
		if _, ok := s[current_max]; ok {
			r = append(r, current_max)
		}
	}

	return r
}

func min(list []int) int {
	min := list[0]
	for _, v := range list {
		if v < min {
			min = v
		}
	}

	return min
}

func max(list []int) int {
	max := 0
	for _, v := range list {
		if v > max {
			max = v
		}
	}

	return max
}