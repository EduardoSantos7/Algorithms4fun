class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = {}

        for piece in pieces:
            index[piece[0]] = piece

        concated = []
        for elem in arr:
            if index.get(elem):
                concated.extend(index.get(elem))

        return concated == arr
