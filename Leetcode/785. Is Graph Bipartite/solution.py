class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        for root in range(0, len(graph)):

            if root in colors:
                continue

            colors[root] = 0
            queue = [root]

            while queue:
                vertice = queue.pop(0)
                edges = graph[vertice]

                for edge in edges:
                    if edge not in colors:
                        queue.append(edge)
                        colors[edge] = 1 - colors[vertice]
                    elif colors[edge] == colors[vertice]:
                        return False

        return True
