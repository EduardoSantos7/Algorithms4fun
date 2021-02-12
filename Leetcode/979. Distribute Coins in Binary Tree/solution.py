# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counter = 0

    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)

            self.counter += abs(l) + abs(r)

            return root.val + l + r - 1
        dfs(root)
        return self.counter
