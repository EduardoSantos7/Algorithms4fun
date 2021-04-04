impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix[0].len();
        let mid = (n as i32) / 2;
        let modul = (n as i32) % 2;

        for i in 0..(mid + modul) {
            for j in (0..mid) {
                let i = i as usize;
                let j = j as usize;
                let tmp = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1];
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }
    }
}
