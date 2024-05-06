class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter_s1 = Counter(s1.split(" "))
        counter_s2 = Counter(s2.split(" "))
        return [w for w, v in counter_s1.items() if v == 1 and w not in counter_s2] + [w for w, v in counter_s2.items() if v == 1 and w not in counter_s1]