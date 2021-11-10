# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if not node1 or not node2:
                return

            if node1 and node2:
                node1.val += node2.val
                dfs(node1.left, node2.left)
                dfs(node1.right, node2.right)

            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        base_root, merge_root = (root1, root2) if root1 else (root2, root1)
        dfs(root1, root2)
        return base_root