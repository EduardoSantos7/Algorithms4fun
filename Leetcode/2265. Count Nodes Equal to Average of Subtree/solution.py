# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans, _, _ = self.averageOfSubtreeDFS(root)
        return ans
    
    def averageOfSubtreeDFS(self, root: TreeNode):
        # leaf node
        if root == None:
            return 0, 0, 0
        
        ans_left, sum_left, nodes_left = self.averageOfSubtreeDFS(root.left)
        ans_right, sum_right, nodes_right = self.averageOfSubtreeDFS(root. right)
        current_sum = root.val + sum_right + sum_left
        current_nodes = 1 + nodes_left + nodes_right
        ans = 1 if root.val == (current_sum // current_nodes) else 0

        return (ans_left + ans_right + ans), current_sum, current_nodes
