class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        freq = Counter(digits)

        for num in range(100, 1000, 2):
            temp_map = dict()
            temp = num
            while temp:
                op = temp % 10
                temp_map[op] = temp_map.get(op, 0) + 1
                temp //= 10

            flag = True
            for i in range(10):
                if temp_map.get(i, 0) > freq.get(i, 0):
                    flag = False
                    break
            
            if flag:
                ans.append(num)

        return ans