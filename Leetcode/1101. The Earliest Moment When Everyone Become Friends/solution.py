class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Sort base on timestamp
        logs = sorted(logs, key=lambda x: x[0])
        # Create groups counter init in n, which will decrease when merging groups
        groups_counter = n
        # Create a map of each person and their group to avoid look ups during group reduction
        groups = {i: set([i]) for i in range(n)}
        # iterate through the logs while there are still logs and groups length is bigger than 1.
        log_index = 0
        while log_index < len(logs):
            # In each iteration identify the two persons becoming friends
            timestamp, person_1, person_2 = logs[log_index]
            log_index += 1
            # If both persons are already in the same group just continue
            if groups[person_1] == groups[person_2]:
                continue
            # If not, merge their groups and set that group to both of them
            groups[person_1].update(groups[person_2])
            groups[person_2].update(groups[person_1])
            groups[person_1] = groups[person_2]
            # update all the groups:
            for k in groups[person_1]:
                groups[k] = groups[person_1]
            groups_counter -= 1
            # print(groups, timestamp, person_1, person_2)

            if groups_counter == 1:
                return timestamp

        return -1