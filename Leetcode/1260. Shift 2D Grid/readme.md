# Algorithm Idea

The algorithm is designed to shift all elements in a 2D grid k positions to the right, wrapping around when necessary. 

1) Initialization:

Determine the number of rows (rows) and columns (cols) in the grid.
Compute the total number of elements (total) in the grid.
Normalize k to ensure it falls within a complete cycle by taking k % total. This avoids unnecessary full rotations.

2) Loop through starting positions:
An outer loop starts from the first element and potentially moves to subsequent elements to begin a new cycle. This loop continues until all elements have been visited.

3) Cycle Detection and Completion:
For each start position, initialize the current position and value to start with.
An inner loop is then used to track and complete a cycle:
Compute the new position (next_index) for the current value using (current_index + k) % total.
Swap the current value into its new position and update the current position to this new position.
Continue this process until the loop returns to the original start position, indicating the cycle is complete.
Increment the count of visited elements.1)
Move to the next start position and repeat until all elements are placed correctly.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Python)

Runtime
127
ms

Beats
59.38%
of users with Python3

Memory
16.99
MB

Beats
58.65%
of users with Python3

Rust)

Runtime
7
ms

Beats
80.00%
of users with Rust

Memory
2.24
MB
Beats
50.00%
of users with Rust

Go)

Runtime
14
ms

Beats
93.51%
of users with Go

Memory
6.86
MB

Beats
79.22%
of users with Go

C)

untime
65
ms

Beats
72.73%
of users with C

Memory
13.57
MB

Beats
100.00%
of users with C