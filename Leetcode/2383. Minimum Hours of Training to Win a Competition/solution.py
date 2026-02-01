class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: List[int],
        experience: List[int],
    ) -> int:
        total_energy = sum(energy)

        curr = 0
        if initialEnergy <= total_energy:
            curr = total_energy - initialEnergy + 1

        res = initialExperience
        for i in experience:
            if i < res:
                res += i
            else:
                train = i - res + 1
                curr += train
                res += train + i

        return curr
