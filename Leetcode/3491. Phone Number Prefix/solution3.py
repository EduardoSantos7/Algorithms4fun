class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        trie = Trie(numbers)

        for number in numbers:
            children = trie.search(number)
            if children["*"] > 1 or len(children) > 1:
                return False

        return True


class Trie:
    def __init__(self, numbers):
        self.trie = dict()
        for number in numbers:
            self.add(number)

    def add(self, number):
        current_level = self.trie
        for digit in number:
            if digit not in current_level:
                current_level[digit] = dict()
            current_level = current_level[digit]

        if "*" not in current_level:
            current_level["*"] = 1
        else:
            current_level["*"] += 1

    def search(self, number):
        current_level = self.trie
        for digit in number:
            if digit in current_level:
                current_level = current_level[digit]
            else:
                return dict()
        return current_level
