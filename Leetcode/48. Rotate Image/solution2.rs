impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        Solution::transpose(matrix);
        Solution::reflect(matrix);
    }

    pub fn transpose(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        let iter = n as i32;
        for i in 0..iter {
            for j in i..iter {
                let i = i as usize;
                let j = j as usize;
                let tmp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }
    }

    pub fn reflect(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        let iter = n as i32;
        for i in 0..iter {
            for j in 0..(iter / 2) {
                let i = i as usize;
                let j = j as usize;
                let tmp = matrix[i][j];
                matrix[i][j] = matrix[i][n - j - 1];
                matrix[i][n - j - 1] = tmp;
            }
        }
    }
}
