class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mem = {}
        curr_max = -inf
        for num in nums:
            if num % 2 is not 0:
                continue
            mem[num] = mem.get(num, 0) + 1

            if mem[num] > curr_max:
                curr_max = mem[num]
        
        possible_ans = []

        for num, freq in mem.items():
            if freq is curr_max:
                possible_ans.append(num)
        
        return possible_ans[0] if len(possible_ans) is 1 else min(possible_ans) if len(possible_ans) > 1 else -1

