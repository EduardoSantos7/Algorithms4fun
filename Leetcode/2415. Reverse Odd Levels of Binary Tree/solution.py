# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        children = []
        level = 0
        flipped = False

        while queue:
            # print(f"Level: {level}", "Start: ", [v.val if not isinstance(v, int) else v  for v in queue], [v.val if not isinstance(v, int) else v  for v in children])
            if level % 2 != 0 and not flipped:
                self._flip(queue)
                flipped = True

            node = queue.pop(0)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            if not queue and children:
                level += 1
                queue.extend(children)
                children = []
                flipped = False
            # print("End: ", [v.val if not isinstance(v, int) else v  for v in queue], [v.val if not isinstance(v, int) else v  for v in children])

        return root

    def _flip(self, queue):
        left, right = 0, len(queue) - 1

        while left < right:
            queue[left].val, queue[right].val = queue[right].val, queue[left].val
            left += 1
            right -= 1
