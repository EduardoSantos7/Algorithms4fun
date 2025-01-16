class Solution:
    def countPairs(self, nums: List[int]) -> int:
        charMap = defaultdict(list)
        res = 0
        maxLen = int(log10(max(nums))) + 1
        chars = [list(str(num).zfill(maxLen)) for num in nums]
        # value of dict is candidates
        for char in chars:
            charMap[''.join(sorted(char))].append(char)
        # print(f'charMap = {charMap}')
        for s in charMap.keys():
            for s1, s2 in combinations(charMap[s], 2):
                if s1 == s2 or sum(s1[i] != s2[i] for i in range(maxLen)) == 2:
                    res += 1
        return res