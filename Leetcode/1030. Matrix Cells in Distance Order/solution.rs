impl Solution {
    pub fn all_cells_dist_order(rows: i32, cols: i32, row_c: i32, col_c: i32) -> Vec<Vec<i32>> {
        let mut res = Vec::with_capacity((rows * cols) as usize);
        for r in 0..rows {
            for c in 0..cols {
                res.push(vec![r, c]);
            }
        }
        res.sort_by_key(|v| (v[0] - row_c).abs() + (v[1] - col_c).abs());
        res
    }
}