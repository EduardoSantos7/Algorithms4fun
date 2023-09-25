# Algorithm Idea

Check in the 4 primary directions (up, down, left, and right) from the position of a rook on a chessboard to see if there's a pawn ("p") that the rook can capture. If there's any other piece (i.e., a piece that's not a pawn and not an empty space "."), then it breaks out of the loop for that direction.

# Complexity

- Time: O(n^2)

- Space:O(1)

# Results

Runtime
38 ms
Beats
72.86%
Memory
16.3 MB
Beats
70.60%