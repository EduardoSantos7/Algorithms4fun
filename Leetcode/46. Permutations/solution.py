class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.generate_permutations(nums, 0, permutations, [], set())
        return permutations

    def generate_permutations(self, nums, index, permutations, current_permutation, seen):
        if len(current_permutation) == len(nums):
            permutations.append(list(current_permutation))

        for i in range(0, len(nums)):
            if nums[i] not in seen:
                current_permutation.append(nums[i])
                seen.add(nums[i])
                self.generate_permutations(nums, index + 1, permutations, current_permutation, seen)
                current_permutation.pop()
                seen.remove(nums[i])