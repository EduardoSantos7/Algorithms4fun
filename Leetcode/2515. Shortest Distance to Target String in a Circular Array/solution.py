class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        
        if target not in words:
            return -1
        
        min_distance = float('inf')
        
        for i in range(n):
            if words[i] == target:
                distance = min(abs(i - startIndex), n - abs(i - startIndex))
                min_distance = min(min_distance, distance)
        
        return min_distance