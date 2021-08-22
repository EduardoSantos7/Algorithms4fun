# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root, acum=0):
            if not root:
                return acum

            root.val += dfs(root.right, acum=acum)
            left_max = dfs(root.left, acum=root.val)

            if root.left:
                return left_max

            return root.val

        dfs(root)

        return root
