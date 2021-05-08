impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let mut count = 0;
        let mut size = flowerbed.len() - 1;
        let mut flowerbed = flowerbed.clone();
        
        for i in 0..flowerbed.len() {
            if flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == size || flowerbed[i+1] == 0) {
                flowerbed[i] = 1;
                count += 1;
            }
            
            if count >= n {
                return true;
            }
        }
        
        false
    }
}