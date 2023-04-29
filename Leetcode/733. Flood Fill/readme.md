# Algorithm Idea

Do DFS through the matrix, if the current point is different from the start color return. If it's the same then update it and do dfs for the pixels connected (4-directionally)

# Complexity

- Time: O(n) - the number of pixels we might process, this can be all the pixels and become mxn

- Space:O(n) - the size of the implicit call stack when calling dfs

# Results

Runtime
80 ms
Beats
42.57%
Memory
16.4 MB
Beats
12.77%