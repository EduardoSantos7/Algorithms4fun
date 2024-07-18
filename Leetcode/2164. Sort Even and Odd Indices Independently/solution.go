import (
	"sort"
)

func sortEvenOdd(nums []int) []int {
	var res []int
	var odd []int
	var even []int

	for i, val := range nums {
		if i%2 == 0 {
			even = append(even, val)
		} else {
			odd = append(odd, val)
		}
	}
	sort.Sort(sort.IntSlice(even))
	sort.Sort(sort.Reverse(sort.IntSlice(odd)))

	for i, val := range odd {
		res = append(res, even[i])
		res = append(res, val)
	}

	if len(even) > len(odd) {
		res = append(res, even[len(even)-1])
	}

	return res
}