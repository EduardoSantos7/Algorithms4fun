class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freqs = Counter(s)
        freqs_target = Counter(target)
        return min([freqs.get(char, 0) // freqs_target.get(char) for char in target])