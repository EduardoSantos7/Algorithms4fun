class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        _set = set()
        _seen = set()
        for w in (s1.split(" ") + s2.split(" ")):
            if w not in _set and w not in _seen:
                _set.add(w)
            elif w in _set:
                _set.remove(w)
                _seen.add(w)
        return _set