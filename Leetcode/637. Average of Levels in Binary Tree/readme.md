# Algorithm Idea

Algorithm 1)

Do BFS and perform the average for each level

Algorithm 2)

Do DFS but pass the level in each iteration, have 2 lists or dicts to keep track the count and sum by level. After traverse the tree do a for to perform the average for each level.

# Complexity

Algorithm 1)

- Time: O(n)

- Space:O(n) # queue might be consider an almost constant complexity in some cases

Algorithm 2)

- Time: O(n)

- Space:O(n) # stack used by recursion

# Results

Algorithm 1)

Runtime
67 ms
Beats
55.54%
Memory
18.9 MB
Beats
72.88%

Algorithm 2)

Runtime
57 ms
Beats
92.67%
Memory
19.5 MB
Beats
15.29%
