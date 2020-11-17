# Algorithm Idea

Builld a graph. Start from the terminal courses (without outgoing edges) and append to queue its dependency if they don't have more outgoing arrows. Decrease the number of courses taken. At the end check if you finish all coursess.

# Complexity

- Time: O(E + V)

- Space:O(E + V)

# Results

- Runtime: 84 ms, faster than 98.80% of Python3 online submissions for Course Schedule.

- Memory Usage: 15.3 MB, less than 79.23% of Python3 online submissions for Course Schedule.