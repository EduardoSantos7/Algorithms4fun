class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        move_left, move_right, any_direction = 0, 0, 0
        for move in moves:
            if move == 'L':
                move_left += 1
            elif move == 'R':
                move_right += 1
            else:
                any_direction += 1
        return max(move_left + any_direction - move_right, move_right + any_direction - move_left)