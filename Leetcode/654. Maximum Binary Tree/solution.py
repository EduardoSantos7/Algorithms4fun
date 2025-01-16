# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.createNodeOfMaximumBinaryTree(nums)
    
    def createNodeOfMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_index = max(enumerate(nums),key=lambda x: x[1])[0]
        root = TreeNode(val = nums[max_index])
        root.left = self.createNodeOfMaximumBinaryTree(nums[:max_index])
        root.right = self.createNodeOfMaximumBinaryTree(nums[max_index + 1:])
        return root