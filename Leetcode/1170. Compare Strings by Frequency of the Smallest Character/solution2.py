import bisect
from typing import List


class Solution:
    # complexity: 2*n^2 + n*logn + 2*n*log(n) -> 2*n^2 + 3*n*logn
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # complexity: n*logn + n*2*l where l is the length of the word -> 2*n^2 + n*logn
        words_freq = sorted([word.count(min(word)) for word in words])

        ans = []

        # complexity: 2*n*log(n)
        for query in queries:
            # complexity: 2*l where l is the length of the word -> 2*n
            query_freq = query.count(min(query))
            # complexity: log(n)
            ans.append(len(words) - bisect.bisect(words_freq, query_freq))

        return ans
