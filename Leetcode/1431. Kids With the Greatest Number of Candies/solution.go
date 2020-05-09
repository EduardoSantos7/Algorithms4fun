func kidsWithCandies(candies []int, extraCandies int) []bool {
	cur_max := max(candies)
	result := make([]bool, len(candies))

	for index, num := range candies {
		if num+extraCandies >= cur_max {
			result[index] = true
		} else {
			result[index] = false
		}
	}

	return result
}

func max(candies []int) int {
	max := 0

	for _, num := range candies {
		if num > max {
			max = num
		}
	}

	return max
}
