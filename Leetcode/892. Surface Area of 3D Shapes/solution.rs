impl Solution {
    pub fn surface_area(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut area = 0;
        let mut nheight = 0;

        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 0 { continue; }

                area += 2;

                let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];
                for &(di, dj) in &directions {
                    let ni = (i as isize + di) as usize;
                    let nj = (j as isize + dj) as usize;

                    if ni < n && nj < n {
                        nheight = grid[ni][nj];
                    } else {
                        nheight = 0;
                    }

                    area += (grid[i][j] - nheight).max(0);
                }
            }
        }
        
        area
    }
}