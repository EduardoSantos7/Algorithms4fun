class TrieNode:
    def __init__(self):
        self.word = ''
        self.is_end = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        for word in words:
            node = self.root
            for char in word:
                node = node.children[char]

            node.is_end = True
            node.word = word

    def longestWord(self):
        queue = [self.root]
        longest = ''

        while queue:
            node = queue.pop(0)

            for child in node.children.values():
                if child.is_end:
                    queue.append(child)

                    if len(child.word) > len(longest) or child.word < longest:
                        longest = child.word
        return longest


class Solution(object):

    def longestWord(self, words):
        trie = Trie()
        trie.insert(words)
        return trie.longestWord()
