impl Solution {
    pub fn shift_grid(mut grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let rows = grid.len();
        let cols = grid[0].len();
        let total = rows * cols;
        let k = (k as usize) % total;

        let mut start = 0;
        let mut count_visited = 0;

        while count_visited < total {
            let mut current_index = start;
            let mut current_value = grid[current_index / cols][current_index % cols];

            loop {
                let next_index = (current_index + k) % total;
                let next_value = grid[next_index / cols][next_index % cols];

                grid[next_index / cols][next_index % cols] = current_value;
                current_index = next_index;
                current_value = next_value;
                count_visited += 1;

                if current_index == start {
                    break;
                }
            }

            start += 1;
        }

        grid
    }
}