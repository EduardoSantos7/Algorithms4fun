class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # Find the index of the words and add it to a list
        pairs = []

        for word in words:
            indexes = self.find_all_indexes(text, word)
            if indexes:
                pairs.extend([[index, index + len(word) - 1] for index in indexes])

        # Sort the list
        pairs_sorted = sorted(pairs, key=lambda x: (x[0], x[1]))
        return pairs_sorted

    def find_all_indexes(self, input_str, search_str):
        """
        Find all indexes of a substring in a string.

        :param input_str: The string to search in.
        :param search_str: The substring to search for.
        :return: A list of indexes where the substring is found.
        """
        indexes = []
        i = input_str.find(search_str)
        while i != -1:
            indexes.append(i)
            i = input_str.find(search_str, i + 1)
        return indexes