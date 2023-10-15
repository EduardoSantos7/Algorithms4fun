"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        neighbors_visited = {node.val: Node(node.val, [])}
        nodes: list = [node]

        while nodes:
            current_node = nodes.pop(0)
            # Create a clone of the current neighbor being visited
            current_clon = neighbors_visited[current_node.val]
            neighbors_visited[current_clon.val] = current_clon
            # Update cloned neighbors with a reference to the new neighbor cloned
            for neighbor in current_node.neighbors:
                if neighbor.val not in neighbors_visited:
                    neighbors_visited[neighbor.val] = Node(neighbor.val, [])
                    nodes.append(neighbor)
                current_clon.neighbors.append(neighbors_visited[neighbor.val])

        return neighbors_visited[node.val]