class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = set(nums) #o(n)
        seen = set()
        max_seq = 0

        for num in mem:
            if num in seen:
                continue
            count = 1
            x = num + 1
            while x in mem:
                count += 1
                seen.add(x)
                x += 1
            max_seq = max(max_seq, count)

            x = num - 1
            while x in mem:
                count += 1
                seen.add(x)
                x -= 1
            max_seq = max(max_seq, count)
            seen.add(num)
        
        return max_seq
