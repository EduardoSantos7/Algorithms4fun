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

        counts = {}
        sums = {}
        ans = []

        def dfs(root, level):
            if not root:
                return

            counts[level] = counts.get(level, 0) + 1
            sums[level] = root.val + sums.get(level, 0)

            dfs(root.left, level+1)
            dfs(root.right, level+1)
            return

        dfs(root, 0)

        for _sum, count in zip(sums.values(), counts.values()):
            ans.append(_sum/count)

        return ans
