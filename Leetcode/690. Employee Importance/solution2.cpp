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
    int ans = 0;
    int getImportance(vector<Employee*> employees, int id){
        for(auto& employee : employees){
            if(employee->id == id) {
                ans += employee->importance;
                for(auto& subordinateId : employee->subordinates) {
                    ans = getImportance(employees, subordinateId);
                }
                break;
            }
        }

        return ans;
    }
};