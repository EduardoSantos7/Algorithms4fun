# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root, "#"]
        temp = []

        while queue:
            element = queue.pop(0)

            if element == "#":
                result.append(temp)
                if len(queue) > 0:
                    queue.append("#")
                    temp = []
                    continue
                else:
                    break
            
            temp.append(element.val)
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
        
        return result
