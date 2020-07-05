package main

func GetNthFib(n int) int {
	if n == 1 {
		return 0
	} else if n == 2 {
		return 1
	}
	return GetNthFib(n-1) + GetNthFib(n-2)
}
