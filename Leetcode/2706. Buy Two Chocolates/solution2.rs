impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        use std::cmp;
        let mut min = cmp::min(prices[0], prices[1]);
        let mut second_min = cmp::max(prices[0], prices[1]);

        for i in 2..prices.len()
        {
            if prices[i] < min
            {
                second_min = min;
                min = prices[i];
            }
            else if prices[i] < second_min
            {
                second_min = prices[i];
            }
        }

        let cost = min + second_min;

        return if cost > money { money } else { money - cost }
    }
}