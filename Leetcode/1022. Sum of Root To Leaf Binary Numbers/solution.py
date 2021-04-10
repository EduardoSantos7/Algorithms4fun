# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, num):
        if not root:
            return 0

        num = num*2 + root.val

        if not root.left and not root.right:
            return num

        return self.dfs(root.left, num) + self.dfs(root.right, num)
