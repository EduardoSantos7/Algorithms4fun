# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # Store the node values in a hashmap where the key is the steps moved from the root and the value is a list of node values
        levels = {}
        # Traverse the tree storing all the nodes in the set
        min_col = 0
        max_col = 0
        queue = [[root, 0]]
        while queue:
            node, col = queue.pop(0)
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            
            if levels.get(col):
                levels[col].append(node.val)
            else:
                levels[col] = [node.val]
            
            if node.left:
                queue.append([node.left, col - 1])
            if node.right:
                queue.append([node.right, col + 1])
        # Create a list of list with the values in the set by ordering the keys
        return [levels[col] for col in range(min_col, max_col + 1)]
