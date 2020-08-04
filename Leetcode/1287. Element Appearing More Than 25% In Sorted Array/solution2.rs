impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let mut count = 0;
        let mut res = 0;
        let size = arr.len();
        
        if size == 1 {
            return arr[0]
        }
        
        for i in 1..arr.len() {
            if arr[i - 1] == arr[i] {
                count += 1;
                if count as f32 / size as f32 > 0.25 {
                    res = arr[i];
                    break
                }
            }
            else {
                count = 1;
            }
        }
        res
    }
}