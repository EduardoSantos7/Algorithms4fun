class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mem = {}
        for i in range(len(names)):
            mem[heights[i]] = names[i]
        
        heights.sort(reverse=True)

        return [mem[h] for h in heights]