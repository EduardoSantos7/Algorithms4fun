# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int, current_path=None, current_total=None) -> List[List[int]]:
        paths = list()
        def dfs(root: Optional[TreeNode], targetSum: int, current_path=None, current_total=None):
            if not root:
                return []
            if not current_path:
                current_path = []
            if not current_total:
                current_total = 0

            current_path.append(root.val)
            current_total += root.val

            if current_total == targetSum and (root.right == None and root.left == None):
                paths.append(list(current_path))

            dfs(root.left, targetSum,  list(current_path), current_total)
            dfs(root.right, targetSum, list(current_path), current_total)
        
        dfs(root, targetSum, current_path, current_total)

        return paths