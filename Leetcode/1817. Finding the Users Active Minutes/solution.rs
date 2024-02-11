use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn finding_users_active_minutes(logs: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut users_by_uam: Vec<i32> = vec![0; k as usize]; // Initialize with zeros
        let mut user_actions: HashMap<i32, HashSet<i32>> = HashMap::new();

        for log in logs 
        {
            let (user_id, action_min) = (log[0], log[1]);

            user_actions
                .entry(user_id)
                .or_insert_with(HashSet::new)
                .insert(action_min);
        }

        let mut total_mins = 0;
        for (user_id, actions) in &user_actions
        {
            total_mins = actions.len();
            users_by_uam[total_mins - 1] += 1;
        }

        users_by_uam
    }
}