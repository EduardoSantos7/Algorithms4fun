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
        self.bfs(root, levels)
        # Create a list of list with the values in the set by ordering the keys
        vertical_levels = []
        sorted_keys = sorted(levels.keys())
        for level in sorted_keys:
            vertical_levels.append(levels[level])

        return vertical_levels

    def bfs(self, root, cols):
        if not root:
            return

        queue = [[root, 0]]
        while queue:
            node, col = queue.pop(0)

            if cols.get(col):
                cols[col].append(node.val)
            else:
                cols[col] = [node.val]

            if node.left:
                queue.append([node.left, col - 1])
            if node.right:
                queue.append([node.right, col + 1])
