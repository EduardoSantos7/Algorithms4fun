class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = {}
        self.count = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = {}
        self.count = 0
        self.trie = TrieNode()

    def insert(self, key: str, val: int) -> None:
        new_val = val - self.values.get(key, 0)
        self.values[key] = val
        cur = self.trie

        for c in key:
            if c not in cur.chars:
                cur.chars[c] = TrieNode()

            cur.chars[c].count += new_val
            cur = cur.chars[c]

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for c in prefix:
            if c not in cur.chars:
                return 0
            cur = cur.chars.get(c)

        return cur.count
