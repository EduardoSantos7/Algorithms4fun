class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        mem = [[x for x in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

        for i in range(1, len(str2) + 1):
            mem[i][0] = mem[i-1][0] + 1

        for row in range(1, len(str2) + 1):
            for col in range(1, len(str1) + 1):
                if str1[col - 1] == str2[row - 1]:
                    mem[row][col] = mem[row-1][col-1]
                else:
                    mem[row][col] = 1 + \
                        min(mem[row][col-1], mem[row-1]
                            [col], mem[row-1][col-1])
        return mem[-1][-1]
