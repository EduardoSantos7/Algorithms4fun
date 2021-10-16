class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        acum = 0
        for op in operations:
            if "+" in op:
                acum += 1
            else:
                acum -= 1
        return acum
