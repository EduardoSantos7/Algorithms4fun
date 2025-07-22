class Solution:
    def countElements(self, arr: List[int]) -> int:
        mem = set(arr)
        counter = 0

        for x in arr:
            if x + 1 in mem:
                counter += 1
        
        return counter