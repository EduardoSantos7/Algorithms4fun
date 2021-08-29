#include <unordered_map>

/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    std::unordered_map<int, Employee*> employeesMap;
    
    int getImportance(vector<Employee*> employees, int id) {
        for(auto& emp : employees){
            employeesMap[emp->id] = emp;
        }

        return dfs(employeesMap[id]);
    }
    
    int dfs(Employee* rootEmployee) {
        if (rootEmployee == NULL) return 0;
        
        vector<int> subsImportance;
        
        for (auto& subId : rootEmployee->subordinates) {
            subsImportance.push_back(dfs(employeesMap[subId]));
        }

        return rootEmployee->importance + accumulate(subsImportance.begin(), subsImportance.end(), 0);
    }
};