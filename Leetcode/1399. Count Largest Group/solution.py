class Solution:
    def countLargestGroup(self, n: int) -> int:

        dp = {0: 0}
        counts = [0] * (4 * 9)
        for i in range(1, n + 1):
            quotient, reminder = divmod(i, 10)
            dp[i] = reminder + dp[quotient]
            counts[dp[i] - 1] += 1

        return counts.count(max(counts))