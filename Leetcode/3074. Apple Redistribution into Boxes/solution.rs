impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, mut capacity: Vec<i32>) -> i32 {
        let total_apples = apple.into_iter().sum();
        capacity.sort_by(|a, b| b.cmp(a));
        let mut i = 0;
        let mut boxes = 0;

        while i < capacity.len() && boxes < total_apples
        {
            boxes += capacity[i];
            i += 1;
        }

        i as i32
    }
}