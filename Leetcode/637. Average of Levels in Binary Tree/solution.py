# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        q = [root]
        ans = []

        while q:
            n = len(q)
            _sum = 0
            count = 0

            for _ in range(n):
                node = q.pop(0)
                if node:
                    _sum += node.val
                    count += 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(_sum/count)

        return ans
