impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        accounts
            .into_iter()
            .map(|banks| banks.into_iter().sum())
            .max()
            .unwrap()
    }
}
