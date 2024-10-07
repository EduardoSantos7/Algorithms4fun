# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val < 2:
            return bool(root.val)
        
        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)

        return left_result or right_result if root.val == 2 else left_result and right_result
        