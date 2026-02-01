# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        queue = [root]
        self.seen = set()

        while queue:
            node = queue.pop()
            self.seen.add(node.val)
            if node and node.left:
                node.left.val = 2 * node.val + 1
                queue.append(node.left)
            if node and node.right:
                node.right.val = 2 * node.val + 2
                queue.append(node.right)

        self.root = root

    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
