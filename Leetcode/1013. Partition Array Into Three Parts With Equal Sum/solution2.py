class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        _sum = sum(arr)
        
        # If after split it the resul is not even then is false
        if _sum % 3 != 0:
            return False

        average, left_sum, right_sum, pl, pr = _sum // 3, arr[0], arr[-1], 1, len(arr) - 2

        while pl <= pr:
            if pl < pr and left_sum != average:
                left_sum += arr[pl]
                pl += 1
            if pl < pr and right_sum != average:
                right_sum += arr[pr]
                pr -= 1
            if left_sum == average == right_sum:
                return True
            if pl == pr:
                return False
        
        return False