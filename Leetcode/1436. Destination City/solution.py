class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}
        for path in paths:

            if path[0] not in cities:
                cities[path[0]] = "s"
            else:
                cities[path[0]] = "s"

            if path[1] not in cities:
                cities[path[1]] = None

        final_city = [key for key, value in cities.items() if not value][0]

        return final_city
