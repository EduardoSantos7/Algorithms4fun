#include <map>

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> mem;
        vector<int> answer;
        
        for(int i = 0; i < nums1.size(); i++) {
            mem[nums1[i]]++;
        }
        
        for(int i = 0; i < nums2.size(); i++) {
            map<int,int>::iterator it = mem.find(nums2[i]);
            if(it != mem.end() && it->second > 0){
                answer.push_back(nums2[i]);
                mem[nums2[i]]--;
            }
        }
        
        return answer;
    }
};