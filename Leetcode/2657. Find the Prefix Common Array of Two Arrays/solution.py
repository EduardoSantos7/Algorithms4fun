class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a_set = set()
        b_set = set()
        ans = [0] * len(A) 
        temp_count = 0

        for i in range(len(A)):
            a_set.add(A[i])

            if A[i] in b_set:
                temp_count += 1
            
            b_set.add(B[i])

            if B[i] in a_set:
                temp_count += 1
        
            ans[i] = temp_count
        
        return ans
