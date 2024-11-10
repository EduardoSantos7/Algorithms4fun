# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root is None or root.left is None:
            return -1
        
        left, right = root.left.val, root.right.val

        # If value is the same as the root then need to find the next candidate.
        if root.left.val == root.val:
            left = self.findSecondMinimumValue(root.left)
        if root.right.val == root.val:
            right = self.findSecondMinimumValue(root.right)
        
        return min(left, right) if left != -1 and right != -1 else left if left != -1 else right
