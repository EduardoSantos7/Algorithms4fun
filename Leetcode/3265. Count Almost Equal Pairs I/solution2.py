class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        freq = Counter()
        for x in nums: 
            ans += freq[x]
            freq[x] += 1
            s = list(str(x).zfill(7))
            for i, j in combinations(range(7), 2): 
                if s[i] != s[j]: 
                    s[i], s[j] = s[j], s[i]
                    cand = int("".join(s))
                    ans += freq[cand] 
                    s[i], s[j] = s[j], s[i]
        return ans