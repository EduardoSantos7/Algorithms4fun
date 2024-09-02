class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([a for a, b in (Counter(arr)).items() if a == b] or [-1])