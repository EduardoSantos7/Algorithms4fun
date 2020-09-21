class Solution(object):
    mem = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.mem:
            ans = []
            for i in range(N):
                # J represent the number of nodes in the right side
                j = N - 1 - i

                # For all possible trees with i nodes
                for left_tree in self.allPossibleFBT(i):
                    # For all possiblle trees with j nodes
                    for right_tree in self.allPossibleFBT(j):
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        ans.append(root)

                Solution.mem[N] = ans

        return Solution.mem[N]
