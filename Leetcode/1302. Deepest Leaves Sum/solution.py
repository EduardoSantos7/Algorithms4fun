# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        work_queue = []
        cur_sum = 0
        
        while queue:
            node = queue.pop(0)
            cur_sum += node.val

            if node.left:
                work_queue.append(node.left)
            if node.right:
                work_queue.append(node.right)
            
            if not queue and work_queue:
                queue = work_queue
                work_queue = []
                cur_sum = 0
            
        return cur_sum
