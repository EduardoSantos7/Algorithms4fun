class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_size_participants = {}

        for participant, group_size in enumerate(groupSizes):
            if group_size_participants.get(group_size):
                group_size_participants[group_size].append(participant)
            else:
                group_size_participants[group_size] = [participant]
        
        people_by_group_size = []

        for group_size, participants in group_size_participants.items():
            group_chunks = [participants[i:i+group_size] for i in range(0, len(participants), group_size)]
            people_by_group_size.extend(group_chunks)
    
        return people_by_group_size