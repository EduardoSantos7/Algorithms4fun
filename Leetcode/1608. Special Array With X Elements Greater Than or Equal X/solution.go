import (
	"math"
)

func specialArray(nums []int) int {
	var n = len(nums)
	var freq = make([]int, n+1)
	var numbersBiggerEqual = 0

	for _, num := range nums {
		freq[int(math.Min(float64(n), float64(num)))] += 1
	}

	for i := n; i >= 0; i-- {
		numbersBiggerEqual += freq[i]
		if numbersBiggerEqual == i {
			return i
		}
	}

	return -1
}