# Algorithm Idea

Approach 1)

Traverse forward through the parents for each side till you find the common.

Approach 2)

Two pointers, till both get to the same node, and once one reach to the end restart it to start as the other pointer

# Complexity

Approach 1)

- Time: O(Max(Depth_p, depth_q))

- Space:O(N)

Approach 1)

- Time: O(Log N)

- Space:O(1)


# Results

Approach 1)

Runtime
53
ms
Beats
38.33%

Memory
20.70
MB
Beats
19.90%

Approach 2)

Runtime
58
ms
Beats
12.87%

Memory
20.95
MB
Beats
10.07%