func oddCells(n int, m int, indices [][]int) int {
	rows := make([]int, n)
	cols := make([]int, m)
	odds := 0

	for _, pos := range indices {
		rows[pos[0]] += 1
		cols[pos[1]] += 1
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if (rows[i]+cols[j])%2 == 1 {
				odds += 1
			}
		}
	}

	return odds
}