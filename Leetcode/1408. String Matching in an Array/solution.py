class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        mem = dict()
        ans = set()

        for word in words:
            n = len(word)
            if n in mem:
                mem[n].append(word)
                continue
            mem[n] = [word]
        
        for word in words:
            i = len(word)
            for j in mem:
                if j < i:
                    continue

                subset = mem.get(j)
                for sw in subset:
                    if sw != word and word in sw and word not in ans:
                        ans.add(word)
        
        return ans
