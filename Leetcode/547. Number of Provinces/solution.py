class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(cities):
            if city in visited:
                continue

            provinces += 1
            self.dfs(isConnected, visited, city)
        
        return provinces
    
    def dfs(self, isConnected, visited, city):
        visited.add(city)

        for neighboard in range(len(isConnected)):
            if isConnected[city][neighboard] and neighboard not in visited:
                self.dfs(isConnected, visited, neighboard)
            
