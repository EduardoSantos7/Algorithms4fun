import (
	"sort"
)

func distinctAverages(nums []int) int {
	sort.Ints(nums)
	averageSeen := make(map[float64]bool)
	i, j := 0, len(nums)-1
	average := 0.0

	for i < j {
		average = float64(nums[i]+nums[j]) / 2.0
		averageSeen[average] = true
		i += 1
		j -= 1
	}

	return len(averageSeen)
}