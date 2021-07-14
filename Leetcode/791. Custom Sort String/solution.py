class Solution:
    def customSortString(self, order: str, str: str) -> str:
        # count chars in str
        mem = {}
        for char in str:
            mem[char] = mem.get(char, 0) + 1

        # traverse order, for each char check if it exists in str and add it the times it appears
        custom_order = []

        for char in order:
            if char in mem:
                custom_order.extend(char * mem.get(char))
                del mem[char]

        for char in mem:
            custom_order.extend(char * mem.get(char))

        return ''.join(custom_order)
