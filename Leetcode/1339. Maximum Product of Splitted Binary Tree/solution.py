# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0

            curr_sum = dfs(root.left) + dfs(root.right) + root.val

            if self.total_sum:
                self.max_prod = max(
                    self.max_prod, (self.total_sum-curr_sum)*curr_sum)

            return curr_sum

        self.total_sum = 0
        self.max_prod = 0
        # Get the total sum
        self.total_sum = dfs(root)
        dfs(root)
        return self.max_prod % (10**9 + 7)
