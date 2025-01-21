class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        seen = set(arr1)
        new_seen = set()
        for num in arr2:
            if num in seen:
                new_seen.add(num)
        seen = new_seen
        new_seen = set()
        for num in arr3:
            if num in seen:
                new_seen.add(num)
        return sorted(list(new_seen))
