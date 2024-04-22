func shiftGrid(grid [][]int, k int) [][]int {
    rows := len(grid)
    cols := len(grid[0])
    total := rows * cols
    k = k % total

    start := 0
    countVisited := 0

    for countVisited < total {
        current_index := start
        current_value := grid[current_index / cols][current_index % cols]

        for {
            next_index := (current_index + k) % total
            next_value := grid[next_index / cols][next_index % cols]

            grid[next_index / cols][next_index % cols] = current_value
            current_index = next_index
            current_value = next_value
            countVisited++

            if current_index == start {
                break
            }
        }

        start++
    }

    return grid
}