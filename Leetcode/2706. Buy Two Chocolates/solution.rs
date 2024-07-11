impl Solution {
    pub fn buy_choco(mut prices: Vec<i32>, money: i32) -> i32 {
        prices.sort();
        let min_cost = prices[0] + prices[1];
        return if min_cost > money { money } else { money - min_cost }
    }
}