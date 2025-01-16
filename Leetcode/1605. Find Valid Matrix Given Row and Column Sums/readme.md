# Algorithm Idea

This algorithm constructs a matrix satisfying given row and column sums by iterating through rows and columns in a two-pointer fashion. At each position, it places the minimum of the current row and column sums, then reduces those sums and advances to the next row or column when a sum reaches zero.

# Complexity

- Time: O(rowsXcolumns)

- Space:O(rowsXcolumns)

# Results

Runtime

21
ms
Beats
81.55%

Memory
22.36
MB
Beats
7.63%