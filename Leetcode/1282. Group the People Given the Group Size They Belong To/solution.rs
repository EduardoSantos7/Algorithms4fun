use std::collections::HashMap;

impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut group_size_participants: HashMap<i32, Vec<i32>> = HashMap::new();

        for (participant, group_size) in group_sizes.into_iter().enumerate()
        {
            group_size_participants
                .entry(group_size)
                .or_insert_with(Vec::new)
                .push(participant as i32)
        }

        let mut people_by_group_size: Vec<Vec<i32>> = Vec::new();

        for (group_size, participants) in group_size_participants
        {
            for chunk in participants.chunks(group_size as usize)
            {
                people_by_group_size.push(chunk.to_vec());
            }
        }

        people_by_group_size
    }
}