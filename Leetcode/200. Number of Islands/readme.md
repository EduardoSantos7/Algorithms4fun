# Algorithm Idea

Approach 1)

Matrix Iteration + DFS/BFS when a 1 is found, using a set to not repeat nodes seen.

Approach 2)

Matrix Iteration + DFS/BFS when a 1 is found, marking visit nodes with zero instead of using a set.

# Complexity

Approach 1)

- Time: O(NxM)

- Space:O(NxM)

Approach 2)

- Time: O(NxM)

- Space:O(1)
  
# Results

Approach 1)

Runtime
295
ms
Beats
16.96%

Memory
25.40
MB
Beats
21.35%

Approach 2)

Runtime
256
ms
Beats
45.29%

Memory
20.13
MB
Beats
53.21%