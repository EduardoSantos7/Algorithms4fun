class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        # Check in rows
        for sub_list in grid:
            # Perfom a binary search in the current sub list
            count += self.binary_search(sub_list)
        return count

    def binary_search(self, sub_list):
        l = 0
        r = len(sub_list) - 1
        ind = -1

        while r >= l:
            mid = l + (r - l) // 2

            if sub_list[mid] >= 0:
                l = mid + 1
            else:
                ind = mid
                r = mid - 1

        return len(sub_list) - ind if ind != -1 else 0
