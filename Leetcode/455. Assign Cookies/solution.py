class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0

        g.sort()
        s.sort()
        counter = 0

        while g and s:
            if s[-1] >= g[-1]:
                counter += 1
                s.pop()
                g.pop()
            else:
                g.pop()

        return counter
