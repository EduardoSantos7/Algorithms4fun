class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        push = []
        dominoes_prev = None

        while dominoes != dominoes_prev:
            dominoes_prev = dominoes
            push = []
            for i, domino in enumerate(dominoes):
                if domino != '.':
                    push.append(domino)
                    continue

                left = dominoes[i-1] if i-1 >= 0 else None
                right = dominoes[i+1] if i+1 < len(dominoes) else None

                if left == "R" and right != "L":
                    push.append("R")
                    continue
                if left != "R" and right == "L":
                    push.append("L")
                    continue

                push.append(domino)

            dominoes = ''.join(push)

        return dominoes
