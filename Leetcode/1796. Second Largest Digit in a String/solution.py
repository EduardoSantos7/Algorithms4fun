class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second_largest = -1

        for c in s:
            if not c.isdigit():
                continue

            c = int(c)

            if c > largest:
                second_largest = largest
                largest = c
            elif c > second_largest and c != largest:
                second_largest = c
        
        return int(second_largest) if largest != second_largest else -1
