# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodesHelper(self, root: TreeNode, expected) -> int:
        if not root:
            return 0

        subtree_expected = (expected - 1) // 2
        right_nodes = self.countNodesHelper(root.right, subtree_expected)

        if right_nodes < subtree_expected:
            left_nodes = self.countNodesHelper(root.left, subtree_expected)
            return left_nodes + right_nodes + 1

        return expected

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Count height
        temp = root
        height = 1

        while temp.left:
            height += 1
            temp = temp.left

        expected = 2 ** height - 1
        nodes = self.countNodesHelper(root, expected)

        return nodes
