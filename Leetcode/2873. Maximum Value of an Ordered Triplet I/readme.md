# Algorithm Idea

Approach 1)

Generate all the triplets using DFS

Approach 2)

Use 3 nested for loops to generate the triplets

Approach 3)

Keep track of the max i and max nums[i] - nums[j] and use a for loop where the current number is num[k] and nums[j]

# Complexity

Approach 1)

- Time: O(3^N)

- Space:O(N)

Approach 2)

- Time: O(N^3)

- Space:O(1)

Approach 3)

- Time: O(N)

- Space:O(1)

# Results

Approach 1)

Runtime
311
ms
Beats
5.08%

Memory
17.25
MB
Beats
6.71%

Approach 2)

Runtime
163
ms
Beats
9.04%

Memory
17.26
MB
Beats
6.71%

Approach 3)

Runtime
0
ms
Beats
100.00%

Memory
17.29
MB
Beats
6.71%