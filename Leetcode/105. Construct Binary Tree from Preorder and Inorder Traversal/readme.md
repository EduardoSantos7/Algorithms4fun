# Algorithm Idea

It will set the first element of preorder as the root, and then construct the entire tree. To find the left and right subtrees, it will look for the root in inorder, so that everything on the left should be the left subtree, and everything on the right should be the right subtree. Both subtrees can be constructed by making another recursion call.

It is worth noting that, while we recursively construct the subtrees, we should choose the next element in preorder to initialize as the new roots. This is because the current one has already been initialized to a parent node for the subtrees.

# Complexity

- Time: O(N)

- Space:O(N)

# Results

Runtime
3
ms
Beats
87.37%

Memory
19.18
MB
Beats
84.42