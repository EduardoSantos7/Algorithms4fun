# Algorithm Idea

Imagine arrows going in 3 directios. Up, Left, UP-Left. The biggest matrix that we can form is the min of the solutions for them plus 1.

Depending the DP approach used you will have to iterate/traverse the matrix, calculate the min value of DPs in the three indexes before mentioned and add 1. That is the solution for the curren i,j. The result is the sum of all dps.

# Complexity

- Time: O(m*n) // traverse all the matrix

- Space:O(m*n) DP

# Results

Bottom-up:

Runtime
568 ms
Beats
95.77%
Memory
18.7 MB
Beats
34.27%

Top-Down:

Runtime
727 ms
Beats
15.12%
Memory
61.1 MB
Beats
5.4%