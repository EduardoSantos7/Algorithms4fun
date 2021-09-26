#include <cmath>

class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> ans;
        for(vector<int> query : queries) {
            int x = query[0], y = query[1], r = query[2];
            int count = 0;
            for (vector<int> point : points) {
                int x1 = point[0], y1 = point[1];
                if (std::pow(x - x1, 2) + std::pow(y - y1, 2) <= std::pow(r, 2)) {
                    count += 1;
                }
            }
            ans.push_back(count);
        }
        return ans;
    }
};