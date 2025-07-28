# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        substrings = []
        queue = [root]
        current_len = 0

        while queue and current_len < k:
            node = queue.pop(-1)
            if node.val:
                substrings.append(node.val)
                current_len += len(node.val)
            else:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return ''.join(substrings)[k-1]
