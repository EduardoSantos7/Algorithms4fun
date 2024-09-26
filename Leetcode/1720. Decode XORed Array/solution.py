class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for elem in encoded:
            arr.append(elem ^ arr[-1])
        return arr