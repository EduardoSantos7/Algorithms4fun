# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        remaining_forest = []
        root = self.dfs(root, set(to_delete), remaining_forest)
        if root:
            remaining_forest.append(root)
        return remaining_forest
    
    def dfs(self, root, to_delete, remaining_forest):
        if not root:
            return None
        
        root.left = self.dfs(root.left, to_delete, remaining_forest)
        root.right = self.dfs(root.right, to_delete, remaining_forest)

        if root.val in to_delete:
            if root.left:
                remaining_forest.append(root.left)
            if root.right:
                remaining_forest.append(root.right)
            return None
        
        return root