class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Sort base on timestamp
        logs = sorted(logs, key=lambda x: x[0])
        # Create groups counter init in n, which will decrease when merging groups
        groups_counter = n
        # Create a map of each person and their group to avoid look ups during group reduction
        groups = UnionFind(n)
        # iterate through the logs while there are still logs and groups length is bigger than 1.

        for timestamp, person_1, person_2 in logs:
            # If both persons are already in the same group just continue
            # If not, merge their groups and set that group to both of them
            if groups.union(person_1, person_2):
                groups_counter -= 1

            if groups_counter == 1:
                return timestamp
        
        return -1

class UnionFind:

    def __init__(self, size):
        self.group = [group_id for group_id in range(size)]
        self.rank = [0] * size

    def find(self, person):
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, a, b):
        """
            return: true if a and b are not connected before
                otherwise, connect a with b and then return false
        """
        group_a = self.find(a)
        group_b = self.find(b)
        is_merged = False
        if group_a == group_b:
            return is_merged

        is_merged = True
        # Merge the lower-rank group into the higher-rank group.
        if self.rank[group_a] > self.rank[group_b]:
            self.group[group_b] = group_a
        elif self.rank[group_a] < self.rank[group_b]:
            self.group[group_a] = group_b
        else:
            self.group[group_a] = group_b
            self.rank[group_b] += 1

        return is_merged