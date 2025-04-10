class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_liters_used = mainTank + min((mainTank-1)//4,additionalTank)
        return 10*total_liters_used