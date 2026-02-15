# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        queue = [root, "#"]
        current_level = 0

        while queue:
            if current_level == level:
                break

            node = queue.pop(0)

            if node == "#":
                current_level += 1
                if queue:
                    queue.append("#")
                    continue
                else:
                    break

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not queue:
            return -1
        queue.pop()  # remove the last marker (#)

        mid = len(queue) // 2
        return queue[mid].val
