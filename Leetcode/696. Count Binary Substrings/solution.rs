impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let (mut curr, mut prev, mut ans) = (1, 0, 0);
        let bytes = s.as_bytes();
        for i in 1..s.len() {
            if bytes[i] == bytes[i -1] { curr += 1; continue; }
            ans += curr.min(prev);
            prev = curr;
            curr = 1;
        }
        return ans + curr.min(prev)
    }
}