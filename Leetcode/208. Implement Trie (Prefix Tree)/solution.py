class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = Trie()
            cur = cur.chars[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for c in word:
            if c not in cur.chars:
                return False
            cur = cur.chars.get(c)

        return cur.is_word == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self
        for c in prefix:
            if c not in cur.chars:
                return False
            cur = cur.chars.get(c)

        return True
