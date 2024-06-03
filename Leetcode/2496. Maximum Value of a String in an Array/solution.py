class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(map(lambda x: int(x) if x.isnumeric() else len(x), strs))