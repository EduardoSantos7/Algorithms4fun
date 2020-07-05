package main

func GetNthFib(n int) int {
	mem := []int{0, 1}

	if n < 3 {
		return mem[n-1]
	}

	new_val := 0
	for x := 3; x < n+1; x++ {
		new_val = mem[0] + mem[1]
		mem[0] = mem[1]
		mem[1] = new_val
	}
	return mem[1]
}
