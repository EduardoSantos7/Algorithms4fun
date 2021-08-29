"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {employee.id: employee for employee in employees}

        def dfs(root_employee):
            if not root_employee:
                return 0
            return root_employee.importance + sum([
                dfs(employees.get(subordinate)) for subordinate in root_employee.subordinates])

        return dfs(employees.get(id))
