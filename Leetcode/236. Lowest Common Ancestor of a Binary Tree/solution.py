# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Set parent pointers
        temp = root
        queue = [temp]
        temp.parent = None
        found_p = False
        found_q = False
        while queue:
            node = queue.pop(0)
            if node.val == p.val:
                found_p == True
            if node.val == q.val:
                found_q == True
            if found_p and found_q:
                break
            if node.left:
                node.left.parent = node
                queue.append(node.left)
            if node.right:
                node.right.parent = node
                queue.append(node.right)

        temp = p
        seen = set([temp.val])
        while temp.parent != None:
            seen.add(temp.parent.val)
            temp = temp.parent

        temp = q
        while temp != None:
            if temp.val in seen:
                return temp
            temp = temp.parent
