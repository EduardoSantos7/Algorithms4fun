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

        neighbors_visited = dict()
        nodes: list = [node]
        copy_reference = None

        while len(nodes) is not 0:
            current_node = nodes.pop(0)

            # Add neighbors to the list of nodes to iterate if hasn't been seen before.
            nodes.extend([neighbor for neighbor in current_node.neighbors if neighbor.val not in neighbors_visited])
            # From the list of original neighbors get the ones that has been already visited (aka cloned)
            neighbors_cloned = [neighbors_visited[neighbor.val] for neighbor in current_node.neighbors if neighbor.val in neighbors_visited]
            # Create a clone of the current neighbor being visited
            current_node_cloned = Node(current_node.val, neighbors_cloned)
            # Update cloned neighbors with a reference to the new neighbor cloned
            for neighbor_cloned in neighbors_cloned:
                neighbors_vals = [neighbor.val for neighbor in neighbor_cloned.neighbors]
                if current_node_cloned.val not in neighbors_vals:
                    neighbor_cloned.neighbors.append(current_node_cloned)
            # Add the new cloned neighbor to the dictionary of nodes visited
            neighbors_visited[current_node_cloned.val] = current_node_cloned
            copy_reference = current_node_cloned

        return neighbors_visited[1]