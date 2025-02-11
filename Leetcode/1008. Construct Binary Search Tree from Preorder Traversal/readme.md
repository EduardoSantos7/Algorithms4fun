# Algorithm Idea

Use a monotonic stack, insert the first node and keep a reference to it since it it's the head. Insert it in to the stack.

then for each next element in the array check if it's smaller than the current top of the stack. If it's add the node as a left child of the top element, if it's bigger keep removing elements till you find one bigger or the stack gets empty. The last element popped will have as right child the current node.

Return the head pointer.

# Complexity

- Time: O(N)

- Space:O(N)

# Results

Runtime
0
ms
Beats
100.00%

Memory
17.72
MB
Beats
49.45%