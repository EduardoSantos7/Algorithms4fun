class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mem = {}
        for item in items1:
            mem[item[0]] = item[1]

        for item in items2:
            if item[0] in mem:
                mem[item[0]] += item[1]
                continue
            mem[item[0]] = item[1]

        ret = []

        for key in sorted(mem.keys()):
            ret.append([key, mem[key]])
        
        return ret