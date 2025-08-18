use std::collections::HashMap;

impl Solution {
    pub fn best_hand(ranks: Vec<i32>, suits: Vec<char>) -> String {
        let mut suits_cards = HashMap::new();
        let mut ranks_cards = HashMap::new();

        for i in 0..5 {
            *suits_cards.entry(suits[i]).or_insert(0) += 1;
            *ranks_cards.entry(ranks[i]).or_insert(0) += 1;
        }

        if suits_cards.len() == 1 {
            return "Flush".to_string();
        }

        let max_rank_count = *ranks_cards.values().max().unwrap();

        if max_rank_count >= 3 {
            return "Three of a Kind".to_string();
        } else if max_rank_count == 2 {
            return "Pair".to_string();
        }

        "High Card".to_string()
    }
}
