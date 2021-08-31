class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort the array
        arr.sort()

        # get the min absolute difference
        min_dif = float('inf')
        for i in range(0, len(arr) - 1):
            min_dif = min(min_dif, abs(arr[i] - arr[i+1]))

        mem = set(arr)
        pairs = []
        pairs_set = set()

        for num in arr:
            small_target = num - min_dif
            bigger_target = num + min_dif

            if small_target in mem:
                pair = (small_target, num)
                if pair in pairs_set:
                    continue
                pairs.append(pair)
                pairs_set.add(pair)

            if bigger_target in mem:
                pair = (num, bigger_target)
                if pair in pairs_set:
                    continue
                pairs.append(pair)
                pairs_set.add(pair)

        return pairs
