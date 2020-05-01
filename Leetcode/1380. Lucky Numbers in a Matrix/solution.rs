use std::collections::HashSet;

impl Solution {
    pub fn lucky_numbers(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut min_nums = HashSet::new();
        let mut res = Vec::new();

        for row in matrix.iter() {
            let mut min = row[0];

            for num in row.iter() {
                if num < &min {
                    min = *num;
                }
            }
            min_nums.insert(min);
        }

        for j in 0..matrix[0].len() {
            let mut current_max = -1;

            for i in 0..matrix.len() {
                let mut num = matrix[i][j];
                if num > current_max {
                    current_max = num;
                }
            }

            if min_nums.contains(&current_max) {
                res.push(current_max);
            }
        }

        return res;
    }
}
