class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        pos_num = len(num) - 1
        acum = 0

        while pos_num >= 0:
            decimal = k % 10
            k //= 10
            new_num = decimal + num[pos_num] + acum

            if new_num > 9:
                num[pos_num] = new_num % 10
                acum = 1
            else:
                num[pos_num] = new_num
                acum = 0

            pos_num -= 1

        missing_to_add = k + acum
        new_in_num = []

        while missing_to_add > 0:
            new_in_num.insert(0, missing_to_add % 10)
            missing_to_add //= 10

        return new_in_num + num
