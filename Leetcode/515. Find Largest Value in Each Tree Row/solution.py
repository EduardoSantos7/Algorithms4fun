# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        row = [root]
        max_in_levels = []

        while row:
            max_in_levels.append(max([node.val for node in row]))

            new_row = []
            for node in row:
                for kid in (node.left, node.right):
                    if kid:
                        new_row.append(kid)
            row = new_row

        return max_in_levels
