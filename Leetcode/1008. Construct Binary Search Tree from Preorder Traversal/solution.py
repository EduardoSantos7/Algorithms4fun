# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(val=preorder[0])
        top = head
        stack = [head]

        for val in preorder[1:]:
            node = TreeNode(val=val)
            if val < top.val:
                top.left = node
            else:
                while top and val > top.val:
                    pop_node = stack.pop()
                    top = stack[-1] if stack else None

                pop_node.right = node
            
            stack.append(node)
            top = node
        
        return head