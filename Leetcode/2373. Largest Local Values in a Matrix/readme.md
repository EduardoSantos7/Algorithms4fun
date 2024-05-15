# Algorithm Idea

We are given an integer matrix grid of size N⋅NN \cdot NN⋅N. For each element (i, j) in the grid, we need to find the maximum value in the 3⋅33 \cdot 33⋅3 matrix with the top left cell as (i, j). The local maximums should be returned in a new matrix. Note that we need to add the value to the new matrix only for (i, j) values with a valid 3⋅33 \cdot 33⋅3 matrix. Therefore, the size of the new matrix is always (N−2)⋅(N−2)(N - 2) \cdot (N - 2)(N−2)⋅(N−2), and the last two rows and columns in the original matrix grid are left out.

We will follow the process given in the problem description to generate the new matrix. 3⋅33 \cdot 33⋅3 matrices cannot be created from the last two rows and last two columns as of grid, so we will iterate over the rows from 0 to N - 2 and columns from 0 to N - 2 in the grid. For each cell, we will iterate over the 3⋅33 \cdot 33⋅3 matrix and find the local maximum value. This value will be stored in the new matrix maxLocal.

# Complexity

- Time: O(n^2)

- Space:O(n^2)

# Results

Runtime
137
ms
Beats
38.94%
of users with Python3

Memory
17.06
MB
Beats
70.33%
of users with Python3