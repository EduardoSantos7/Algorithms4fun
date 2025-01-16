class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        total_groups, incomplete_group = divmod(len(s), k)
        ans = [s[i*k:i*k + k] for i in range(total_groups)]
        if incomplete_group:
            ans.append(s[-incomplete_group:].ljust(k, fill))
        return ans