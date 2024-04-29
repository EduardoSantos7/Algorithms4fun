impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        let mut arr2 = arr2;
        arr2.sort_unstable();
        let mut result = 0;
        for x in arr1 {
            let l = x - d;
            let r = x + d;
            let li = match arr2.binary_search(&l) {
                Ok(pos) => pos,
                Err(pos) => pos,
            };
            let ri = match arr2.binary_search(&r) {
                Ok(pos) => pos,
                Err(pos) => pos,
            };
            if li == ri && (li == arr2.len() || arr2[li] > r) {
                result += 1;
            }
        }
        result
    }
}