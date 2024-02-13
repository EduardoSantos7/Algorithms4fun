func countDistinctIntegers(nums []int) int {
	distinctNums := make(map[int]bool)
	for _, num := range nums {
		distinctNums[num] = true
		reversedNum, _ := strconv.Atoi(reverseNumber(num))
		distinctNums[reversedNum] = true
	}
	return len(distinctNums)
}

func reverseNumber(num int) string {
	numStr := strconv.Itoa(num)
	reversed := ""
	for i := len(numStr) - 1; i >= 0; i-- {
		reversed += string(numStr[i])
	}
	return reversed
}