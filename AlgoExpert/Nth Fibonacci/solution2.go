package main

func GetNthFib(n int) int {
	return helper(n, map[int]int{
		1: 0,
		2: 1,
	})
}

func helper(n int, mem map[int]int) int {
	if val, found := mem[n]; found {
		return val
	}
	mem[n] = helper(n-1, mem) + helper(n-2, mem)
	return mem[n]
}
