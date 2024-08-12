class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mem_a = Counter([c for c in s[:len(s)//2] if c.lower() in "aeiou"])
        mem_b = Counter([c for c in s[len(s)//2:] if c.lower() in "aeiou"])
        return sum(mem_a.values()) == sum(mem_b.values())