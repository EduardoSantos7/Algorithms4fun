class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st1 = sum(students)
        st0 = len(students) - st1
        sa1 = sum(sandwiches)
        sa0 = len(sandwiches) - sa1
        # find the bottleneck
        if st1 == sa1:
            return 0
        if st1 > sa1:
            # 0 is the bottleneck
            count = 0
            for i in range(len(sandwiches)):
                if sandwiches[i] == 0:
                    if count == st0:
                        return len(students) - i
                    count += 1
        elif st0 > sa0:
            count = 0
            for i in range(len(sandwiches)):
                if sandwiches[i] == 1:
                    if count == st1:
                        return len(students) - i
                    count += 1