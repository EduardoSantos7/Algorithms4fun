# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        q = [root]
        while q and level:
            newQ = []
            for node in q:
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
            q = newQ
            level -= 1
        return q[len(q)//2].val if q else -1
