impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let mut r_count = 0;
        let mut d_count = 0;

        let mut r_pending_ban = 0;
        let mut d_pending_ban = 0;

        // queue of senators
        let mut queue = Vec::new();
        for c in senate.chars() {
            queue.push(c);
            if c == 'R' { r_count += 1; } else { d_count += 1; }
        }

        // While any party has eligible senators
        while r_count > 0 && d_count > 0 {    
            let curr = queue.remove(0);

            if curr == 'D'{
                if d_pending_ban > 0 {
                    d_pending_ban -= 1;
                    d_count -= 1;
                } else {
                    r_pending_ban += 1;
                    queue.push('D');
                }
            } else{
                if r_pending_ban > 0 {
                    r_pending_ban -= 1;
                    r_count -= 1;
                } else {
                    d_pending_ban += 1;
                    queue.push('R');
                }
            }
        }

        if r_count > 0 { return "Radiant".to_string(); } else { return "Dire".to_string(); }
    }
}