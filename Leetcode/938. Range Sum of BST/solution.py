# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        queue = [root]
        while queue:
            node = queue.pop()
            if not node:
                continue
            if node.val >= low and node.val <= high:
                result += node.val
            
            if low < node.val:
                queue.append(node.left)
            if node.val < high:
                queue.append(node.right)
        
        return result