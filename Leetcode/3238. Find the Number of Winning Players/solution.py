class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        players = []
        for _ in range(n):
            players.append(dict())

        for move in pick:
            players[move[0]][move[1]] = players[move[0]].get(move[1], 0) + 1

        winners = 0
        for player in range(n):
            if any(filter(lambda x: x > player, players[player].values())):
                winners += 1

        return winners
