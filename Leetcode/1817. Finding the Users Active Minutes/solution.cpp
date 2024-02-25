#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        std::unordered_map<int, std::unordered_set<int>> userActions;

        for (const auto& log : logs)
        {
            int userId = log[0];
            int actionMin = log[1];

            userActions[userId].insert(actionMin);
        }

        std::vector<int> usersByUAM(k, 0);
        for (const auto& actions : userActions) 
        {
            int totalMins = actions.second.size();
            usersByUAM[totalMins - 1]++;
        }

        return usersByUAM;
    }
};