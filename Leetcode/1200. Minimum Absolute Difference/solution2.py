class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort the array
        arr.sort()

        min_dif = float("inf")
        prev_num = arr[0]
        pairs = []

        for i in range(1, len(arr)):
            cur_dif = arr[i] - prev_num

            if cur_dif < min_dif:
                pairs.clear()
                min_dif = cur_dif
                pairs.append((prev_num, arr[i]))
            elif cur_dif == min_dif:
                pairs.append((prev_num, arr[i]))

            prev_num = arr[i]

        return pairs
