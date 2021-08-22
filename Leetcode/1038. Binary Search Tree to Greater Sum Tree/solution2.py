# Same algorithm as first method but this is cleaner

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    acum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        self.bstToGst(root.right)

        root.val += self.acum
        self.acum = root.val

        self.bstToGst(root.left)

        return root
