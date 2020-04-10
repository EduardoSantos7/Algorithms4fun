func minTimeToVisitAllPoints(points [][]int) int {
	if len(points) == 1 {
		return 0
	}

	total := 0

	for i := 1; i < len(points); i += 1 {
		last := points[i-1]
		current := points[i]
		difX := abs(current[0] - last[0])
		difY := abs(current[1] - last[1])
		total += max(difX, difY)
	}
	return total
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}