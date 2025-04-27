# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonely_node = []
        queue = [root]

        while queue:
            node = queue.pop()
            if node.right and not node.left:
                lonely_node.append(node.right.val)
            if node.left and not node.right:
                lonely_node.append(node.left.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return lonely_node
