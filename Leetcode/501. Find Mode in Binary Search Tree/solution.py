# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = self.get_freq_using_bfs(root)
        max_val = max(freq.values())
        return [key for key in freq if freq[key] == max_val]

    def get_freq_using_bfs(self, root: Optional[TreeNode]):
        stack = [root]
        freq = {}
        while stack:
            root = stack.pop()
            freq[root.val] = freq.get(root.val, 0) + 1
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return freq
