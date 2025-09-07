class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        benches = dict()
        for (student, bench) in students:
            if bench in benches:
                benches[bench].add(student)
            else:
                benches[bench] = set([student])
        ans = 0
        for students in benches.values():
            ans = max(ans, len(students))

        return ans
