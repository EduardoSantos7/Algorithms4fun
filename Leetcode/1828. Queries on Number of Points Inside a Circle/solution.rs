impl Solution {
    pub fn count_points(points: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = Vec::new();

        for query in queries {
            let (x, y, r) = (query[0], query[1], query[2]);
            let mut count = 0;
            for point in &points {
                let (x1, y1) = (point[0], point[1]);
                if (x - x1).pow(2) + (y - y1).pow(2) <= r.pow(2) {
                    count += 1;
                }
            }

            ans.push(count);
        }

        ans
    }
}
