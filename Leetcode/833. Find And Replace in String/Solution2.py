class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        p = 0
        n = len(S)
        movements = [0] * n
        for i, source, target in sorted(zip(indexes, sources, targets), reverse=True):

            p = movements[i]
            if S[i + p: i + p + len(source)] == source:
                S = S[:i + p] + target + S[i + p + len(source):]

            movs = len(target) - len(source)
            for pos in range(i, n):
                movements[pos] += movs

        return S
