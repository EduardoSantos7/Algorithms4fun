class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # tranform list of edges to a map for easier look up
        edges_map = {}
        for edge in edges:
            if edge[0] in edges_map:
                edges_map[edge[0]].add(edge[1])
            else:
                edges_map[edge[0]] = set([edge[1]])
            if edge[1] in edges_map:
                edges_map[edge[1]].add(edge[0])
            else:
                edges_map[edge[1]] = set([edge[0]])

        # BFS from source to destination
        queue = [source]
        seen = set()

        while queue:
            node = queue.pop(0)
            if node == destination:
                return True
            if node in seen:
                continue
            seen.add(node)
            for child in edges_map[node]:
                if child not in seen:
                    queue.append(child)

        return False