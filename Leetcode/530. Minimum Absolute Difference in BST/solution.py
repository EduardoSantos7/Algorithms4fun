class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.__get_minimum_diff(root, -maxsize, maxsize)

    @classmethod
    def __get_minimum_diff(cls, tree: TreeNode | None, lo: int, hi: int) -> int:
        if tree is None:
            return hi - lo
        return min(
            cls.__get_minimum_diff(tree.left, lo, tree.val),
            cls.__get_minimum_diff(tree.right, tree.val, hi),
        )
