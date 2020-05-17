class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, end = map(set, zip(*paths))
        return (end - start).pop()
