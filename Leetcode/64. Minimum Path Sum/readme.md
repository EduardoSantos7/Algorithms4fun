# Algorithm Idea

Dynamic Programming: In this case you can update the value of every cell in the matrix like this:

value = value + min(up, left)

and the answer will be in the target cell.

# Complexity

- Time: O(N*M)

- Space:O(1)

# Results

Runtime
20
ms
Beats
31.73%

Memory
19.94
MB
Beats
75.10%
