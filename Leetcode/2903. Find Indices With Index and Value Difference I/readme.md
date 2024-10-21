# Algorithm Idea

Approach 1)

For each number traverse the array comparinf the index difference and value difference, if it's bigger or equal than required return those indexes.

Approach 2)

Instead of comparing all possible pairs of indices using two nested loops, the solution maintains only the necessary information (minimum and maximum values) from within a moving window.

# Complexity

Approach 1)

- Time: O(N^2)

- Space:O(1)

Approach 2)

# Results

Approach 1)

Runtime
3
ms
Beats
99.18%

Memory
16.53
MB
Beats
52.67%

Approach 2)

Runtime
0
ms
Beats
100.00%

Memory
16.70
MB
Beats
12.35%