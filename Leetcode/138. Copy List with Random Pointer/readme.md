# Algorithm Idea

Approach 1)

Use an array to record the random pointer for each node, saving its index then recreate these nodes and fix their pointers

Approach 2)

To avoid the use of linear memory, substitute the arrays by placing the nodes in front of the original node and then re arrange pointers

# Complexity

Approach 1)

- Time: O(N)

- Space:O(N)

Approach 2)

- Time: O(N)

- Space:O(1)

# Results

Approach 1)

Runtime
40
ms
Beats
65.88%

Memory
18.60
MB
Beats
37.84%

Approach 2)

Runtime
41
ms
Beats
56.97%

Memory
18.47
MB
Beats
77.22%
