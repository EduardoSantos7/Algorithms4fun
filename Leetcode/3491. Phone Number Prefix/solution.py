class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        mem = set()

        for number in numbers:
            if number in mem:
                return False

            for recorded_num in mem:
                if recorded_num.startswith(number):
                    return False
                if number.startswith(recorded_num):
                    return False

            mem.add(number)

        return True
