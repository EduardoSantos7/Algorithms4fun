class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        seen_paths = dict()
        n = 0
        for node in range(n + 1):
            seen_paths[n] = self.get_paths(n, graph, seen_paths)
        
        all_paths = []
        for paths in seen_paths.values():
            all_paths.extend(paths)
        return all_paths
    
    def get_paths(self, node: int, graph: List[List[int]], seen_paths: dict):
        paths = []
        queue=[[0]]
        target = len(graph) - 1
        while len(queue) > 0:
            visiting_node = queue.pop(0)

            if visiting_node[-1] == target:
                paths.append(visiting_node)
                continue
            
            #exapnd top 
            for n in graph[visiting_node[-1]]:
                queue.append(visiting_node + [n])
        return paths
