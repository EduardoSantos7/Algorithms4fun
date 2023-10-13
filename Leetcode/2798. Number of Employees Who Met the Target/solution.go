func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
    count := 0
    for _, h := range hours {
        if h >= target {
            count++
        }
    }
    return count
}