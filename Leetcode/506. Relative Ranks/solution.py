class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        sorted_scores = sorted(scores, reverse=True)
        ans = []

        for score in scores:
            i = sorted_scores.index(score)
            rank = "Gold Medal" if i == 0 else "Silver Medal" if i == 1 else "Bronze Medal" if i == 2 else str(i + 1)
            ans.append(rank)
        
        return ans