class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mem = set()
        for i in range(len(arr)):
            if (arr[i] * 2) in mem:
                return True

            if (arr[i] % 2 == 0) and (arr[i] // 2) in mem:
                return True
            
            mem.add(arr[i])

        return False