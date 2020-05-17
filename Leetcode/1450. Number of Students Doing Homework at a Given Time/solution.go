func busyStudent(startTime []int, endTime []int, queryTime int) int {
	students := 0
	for i := 0; i < len(startTime); i++ {
		if startTime[i] <= queryTime && endTime[i] >= queryTime {
			students += 1
		}
	}
	return students
}