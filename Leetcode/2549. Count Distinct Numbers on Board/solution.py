class Solution:
    def distinctIntegers(self, n: int) -> int:
        board = set([n])  # set of list of n
        queue = [n]  # queue is a list of n

        while queue:
            next_queue = []
            for x in queue:
                for i in range(1, n + 1):
                    if x % i == 1 and i not in board:
                        board.add(i)
                        next_queue.append(i)

            queue = next_queue  # proceed to next round

        return len(board)
