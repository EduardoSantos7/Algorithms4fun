class Solution:
    # complexity: 2*n^2 + 4*n^2 -> 8*n^2
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # complexity: n*2*l where l is the length of the word -> 2*n^2
        words_freq = {
            word: word.count(min(word)) for word in words
        }

        queries_freq = {}

        ans = []

        # complexity: q*4*n where q is the length of queries -> 4n^2
        for query in queries:
            if query in queries_freq:
                ans.append(queries_freq[query])
                continue

            # complexity: 2*l where l is the length of the word -> 2*n
            query_freq = query.count(min(query))
            # complexity: n*n due the iteration and the sum -> 2*n
            num = sum([1 if query_freq < words_freq[word]
                       else 0 for word in words])
            ans.append(num)
            queries_freq[query] = num

        return ans
