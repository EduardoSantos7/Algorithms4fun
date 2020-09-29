# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = [root]

        while stack:
            current = stack.pop()

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            if stack:
                current.right = stack[-1]

            current.left = None
