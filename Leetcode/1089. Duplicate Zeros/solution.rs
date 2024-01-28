impl Solution {
    pub fn duplicate_zeros(arr: &mut Vec<i32>) {
        let mut possible_dups = 0;
        let mut length = arr.len() - 1;

        // Find the number of zeros to be duplicated
        for left in 0..(length + 1)
        {
            if left > length - possible_dups { break }

            if arr[left as usize] == 0
            {
                if left == (length - possible_dups)
                {
                    arr[length as usize] = 0;
                    length -= 1;
                    break
                }

                possible_dups += 1;
            }
        }

        let last = length - possible_dups;

        // Copy zero twice, and non zero once.
        for i in (0..=last).rev()
        {
            if arr[i] == 0
            {
                arr[i + possible_dups] = 0;
                possible_dups -= 1;
                arr[i + possible_dups] = 0;
            } 
            else 
            {
                arr[i + possible_dups] = arr[i];
            }
        }
    }
}