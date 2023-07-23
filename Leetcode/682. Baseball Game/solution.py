class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []

        for operation in operations:
            if operation == "+":
                nums.append(sum(nums[-2:]))
                continue
            if operation == "D":
                nums.append(nums[-1] * 2)
                continue
            if operation == "C":
                nums.pop()
                continue
            nums.append(int(operation))

        return sum(nums)
