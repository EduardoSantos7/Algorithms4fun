from collections import deque


class Solution:
    def reverseOddLevels(self, root):
        queue = deque([root, True])  # use deque instead of list
        level = 0

        while queue:
            node = queue.popleft()  # O(1) instead of O(n)

            if isinstance(node, bool):
                level += 1
                if level % 2 != 0:
                    left, right = 0, len(queue) - 1
                    while left < right:
                        queue[left].val, queue[right].val = (
                            queue[right].val,
                            queue[left].val,
                        )
                        left += 1
                        right -= 1
                if queue:
                    queue.append(True)
                continue

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
