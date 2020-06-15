package main

func TwoNumberSum(array []int, target int) []int {
	mem := make(map[int]int)
	res := make([]int, 0)
	for _, num := range array {
		if _, ok := mem[target-num]; ok {
			res = append(res, num)
			res = append(res, target-num)
			return res
		}
		mem[num] = 1
	}
	return res
}
