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

        while queue:
            children = []
            # print(f"Level: {level}", "Start: ", [v.val if not isinstance(v, int) else v  for v in queue])
            for i, node in enumerate(queue):
                if level % 2 != 0 and i < (len(queue) // 2):
                    queue[i].val, queue[len(queue) - i - 1].val = (
                        queue[len(queue) - i - 1].val,
                        queue[i].val,
                    )
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            level += 1
            queue = children
            # print("End: ", [v.val if not isinstance(v, int) else v  for v in queue])

        return root
