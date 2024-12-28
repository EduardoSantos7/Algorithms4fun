class Solution:
    def maxLength(self, arr: List[str]) -> int:
        results = [""]
        best = 0
        for word in arr:
            for i in range(len(results)):
                new_res = results[i] + word
                if len(new_res) != len(set(new_res)):
                    continue
                
                results.append(new_res)
                best = max(best, len(new_res))
        
        return best