# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False

            if root.val == subRoot.val and is_equal(root.left, subRoot.left) and is_equal(root.right, subRoot.right):
                return True

        def check_all(root, subRoot):
            return is_equal(root, subRoot) or (root.left and check_all(root.left, subRoot)) or (root.right and check_all(root.right, subRoot))

        return check_all(root, subRoot)
