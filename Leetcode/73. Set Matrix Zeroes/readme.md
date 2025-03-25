# Algorithm Idea

Approach 1)

Use sets to record where the zeros are to later iterate the matrix again to set those columns and rows to zeros

Approach 2)

Use the first col and row to keep track of which should be set to zero.

# Complexity

Approach 1)

- Time: O(MxN)

- Space:O(M+N)

Approach 2)

- Time: O(MxN)

- Space:O(1)

# Results

Approach 1)

Runtime
2
ms
Beats
76.69%

Memory
18.39
MB
Beats
79.42%

Approach 2)

Runtime
0
ms
Beats
100.00%

Memory
18.53
MB
Beats
39.59%