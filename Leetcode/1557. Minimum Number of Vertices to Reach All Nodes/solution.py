class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming_edges = [0] * n

        for pair in edges:
            incoming_edges[pair[1]] += 1

        return {node for node in range(n) if not incoming_edges[node]}
