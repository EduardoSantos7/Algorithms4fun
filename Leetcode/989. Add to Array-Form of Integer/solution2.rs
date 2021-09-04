impl Solution {
    pub fn add_to_array_form(mut num: Vec<i32>, mut k: i32) -> Vec<i32> {
        let mut pos_num: i32 = num.len() as i32 - 1;
        let mut missing_to_add = 0;
        let mut news: Vec<i32> = Vec::new();
        let mut acum = 0;
        
        while pos_num >= 0 {
            let mut decimal = k % 10;
            k /= 10;
            let mut new_num = decimal + num[pos_num as usize] + acum;

            if (new_num > 9){
                num[pos_num as usize] = new_num % 10;
                acum = 1;   
            }
            else{
                num[pos_num as usize] = new_num;
                acum = 0;   
            }

            pos_num -= 1;
        }
        
        missing_to_add = k + acum;

        while missing_to_add > 0{
            news.push(missing_to_add % 10);
            missing_to_add /= 10;
        }
        
        news.reverse();
        
        news.into_iter().chain(num.into_iter()).collect()
        
    }
}