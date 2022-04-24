# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def traverse(root):
            if not root:
                return 0, 0
            node_sum_left, tilt_left = traverse(root.left)
            node_sum_right, tilt_right = traverse(root.right)

            current_sum = root.val + node_sum_left + node_sum_right
            current_tilt = abs(node_sum_left - node_sum_right) + \
                tilt_left + tilt_right

            return current_sum, current_tilt

        _, current_tilt = traverse(root)

        return current_tilt
