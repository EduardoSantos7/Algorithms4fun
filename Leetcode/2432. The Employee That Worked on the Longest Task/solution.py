class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        durations = []
        last_time = 0

        for task_info in logs:
            durations.append(task_info[1] - last_time)
            last_time = task_info[1]
        
        max_duration = max(durations)
        tasks = [i for i in range(len(durations)) if  durations[i] == max_duration]
        min_id = min([logs[task_id][0] for task_id in tasks])
        return min_id
