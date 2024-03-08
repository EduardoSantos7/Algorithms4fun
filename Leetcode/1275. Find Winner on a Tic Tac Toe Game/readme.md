# Algorithm Idea

Instead of harcoding 3 all over the place. Solve for n * n grid and set n = 3 in the beginning. That way the code is scalable.

Storing the rows and cols as array of size n + 2 variables for diagonals and reverse diagonal. This requires less memory O(2n + 2) instead of O(n^2)

Also checking if a player has won or not takes O(1) time as I have to check 4 variables.

The logic is to increment(Player A) and decrement(Player B) the row, col and the 2 diagonal variables depending on who played and which row, col was played.

After every move, we need to check if the value of the row, col, or the diagonal variables is 3 or -3. Whoever played in that turn is the winner.

# Complexity

- Time: O(N) where N is the total steps, O(1) every step

- Space:O(n) where n is the size of the matrix (n x n)

# Results

Runtime
35
ms
Beats
75.80%
of users with Python3

Memory
16.68
MB
Beats
44.79%
of users with Python3