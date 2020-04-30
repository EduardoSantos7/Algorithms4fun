func sumZero(n int) []int {
	var loop int = n/2 + 1
	rem := n % 2
	res := make([]int, 0)

	if rem == 1 {
		res = append(res, 0)
	}

	for i := 1; i < loop; i++ {
		res = append(res, i, -i)
	}

	return res
}