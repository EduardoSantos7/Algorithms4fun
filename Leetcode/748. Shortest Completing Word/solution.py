class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        shortest_completing_word = ''
        license_plate_counter = Counter([c for c in licensePlate.lower() if c.isdigit() is False and c is not ' '])
 
        for word in words:
            sanitazied_word = Counter([c for c in word.lower() if c.isdigit() is False and c is not ' '])
            valid = True
            for c in license_plate_counter:
                if sanitazied_word.get(c, 0) < license_plate_counter[c]:
                    valid = False
                    break
            if valid and len(word) < len(shortest_completing_word):
                shortest_completing_word = word
            elif valid and not shortest_completing_word:
                shortest_completing_word = word

        return shortest_completing_word