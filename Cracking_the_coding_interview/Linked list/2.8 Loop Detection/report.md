# Problem

Return the node which is the start of the loop

# Algorithm Idea

Use a fast and slow pointer to detect the loop, then move the slow pointer to the head and keep the fast pointer in the collision node. Then move both pointers one step per iteration. When both pointer are in the same node, return that node.

# Complexity

- Time: O(N)

- Space:O(1)
