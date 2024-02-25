class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users_by_uam = [0] * k
        user_actions = {}

        for log in logs:
            user_id, action_min = log
            if user_actions.get(user_id):
                user_actions[user_id].add(action_min)
            else:
                user_actions[user_id] = set([action_min])

        for _, actions in user_actions.items():
            total_mins = len(actions)
            users_by_uam[total_mins - 1] += 1
        
        return users_by_uam