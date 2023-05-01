class Solution:
    def average(self, salary: List[int]) -> float:
        max_s = salary[0]
        min_s = salary[0]
        total = 0
        for s in salary:
            total += s
            if s > max_s:
                max_s = s
                continue
            if s < min_s:
                min_s = s
        return (total - max_s - min_s) / (len(salary) - 2)
