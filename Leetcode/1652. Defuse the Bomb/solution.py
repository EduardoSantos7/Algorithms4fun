class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        p1 = 1 if k > 0 else len(code) - 1
        p2 = k if k > 0 else len(code) + k

        p1, p2 = (p1, p2) if p1 < p2 else (p2, p1)

        cur_sum = sum(code[p1:p2 + 1])
        out = []

        for i, num in enumerate(code):
            out.append(cur_sum)
            cur_sum -= code[p1]
            p1 = (p1 + 1) % len(code)
            p2 = (p2 + 1) % len(code)
            cur_sum += code[p2]

        return out
