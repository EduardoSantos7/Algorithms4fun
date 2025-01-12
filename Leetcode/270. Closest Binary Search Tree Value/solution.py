# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float, min_dif: float = float('inf'), min_val: float = None) -> int:
        if not root:
            return min_val

        temp_dif = abs(root.val - target)

        if temp_dif < min_dif:
            min_dif = temp_dif
            min_val = root.val
        elif temp_dif == min_dif:
            min_val = min(min_val, root.val)

        if root.left is None and root.right is None:
            return min_val

        if root.val > target:
            min_val = self.closestValue(root.left, target, min_dif, min_val)
        else:
            min_val = self.closestValue(root.right, target, min_dif, min_val)

        return min_val