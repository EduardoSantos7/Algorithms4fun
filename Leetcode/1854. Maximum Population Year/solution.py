class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        temp = [0] * 2051
        for log in logs:
            temp[log[0]] += 1
            temp[log[1]] -= 1
        
        _max, ans = temp[1950], 1950

        for i in range(1951, 2051):
            temp[i] += temp[i - 1]

            if temp[i] > _max:
                _max = temp[i]
                ans = i
        
        return ans