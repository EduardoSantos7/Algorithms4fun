class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = 0
        cache = dict()
        for a, b in dominoes:
            pair = (a, b) if a < b else (b, a)
            cache[pair] = cache.get(pair, 0) + 1

        return sum([value*(value-1)//2 for value in cache.values() if value > 0])