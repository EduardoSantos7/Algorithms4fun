impl Solution {
    pub fn minimum_cost(mut cost: Vec<i32>) -> i32 {
        let mut res = 0;
        cost.sort_by(|a, b| b.cmp(a));
        for triplet in cost.chunks(3) {
            res += triplet.get(0).unwrap_or(&0) + triplet.get(1).unwrap_or(&0);
        }
        res
    }
}