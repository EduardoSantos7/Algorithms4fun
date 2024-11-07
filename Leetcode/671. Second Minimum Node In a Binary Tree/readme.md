# Algorithm Idea

recursively traversing the binary tree in a selective manner, leveraging the special property of the tree where root.val = min(root.left.val, root.right.val).

Here's how it operates:

Base Case: If the current node is None or it's a leaf node (since every node has either 0 or 2 children, checking root.left is None suffices), return -1.

Initial Values:

Set left and right to the values of root.left.val and root.right.val, respectively.
Recursive Traversal:

If root.left.val equals root.val, recursively search the left subtree for a candidate.
If root.right.val equals root.val, recursively search the right subtree for a candidate.
Determine the Second Minimum:

Return the minimum of left and right if both are valid (!=-1).
If only one is valid, return that one.
If neither is valid, return -1.

# Complexity

- Time: O(N)

- Space:O(D)

# Results

Runtime
0
ms
Beats
100.00%

Memory
16.62
MB
Beats
16.52%