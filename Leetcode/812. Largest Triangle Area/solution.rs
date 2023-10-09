impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        let mut max_area = 0.0;
        let n = points.len();

        for i in 0..n - 2 {
            for j in i + 1..n - 1 {
                for k in j + 1..n {
                    let x1 = points[i][0] as f64;
                    let y1 = points[i][1] as f64;
                    let x2 = points[j][0] as f64;
                    let y2 = points[j][1] as f64;
                    let x3 = points[k][0] as f64;
                    let y3 = points[k][1] as f64;

                    let area = 0.5 * f64::abs(x1 * (y2-y3) + x2 * (y3 - y1) + x3 * (y1 - y2));
                    max_area = f64::max(max_area, area)
                }
            }
        }

        max_area
    }
}