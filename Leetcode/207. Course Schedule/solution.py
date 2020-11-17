class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        in_degree = [0] * numCourses

        for i in range(numCourses):
            graph[i] = []

        for course_pair in prerequisites:
            graph[course_pair[0]].append(course_pair[1])
            in_degree[course_pair[1]] += 1

        queue = [course for course in range(
            numCourses) if in_degree[course] == 0]

        while queue:
            course = queue.pop(0)

            for dependency in graph[course]:
                in_degree[dependency] -= 1

                if not in_degree[dependency]:
                    queue.append(dependency)

            numCourses -= 1

        return numCourses == 0
