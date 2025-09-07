#include <iostream>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool confusingNumber(int n) {
        // Convert number to string
        std::string str_n = std::to_string(n);
        
        // Map of valid rotations
        std::unordered_map<char, char> rotate_map = {
            {'0', '0'},
            {'1', '1'},
            {'6', '9'},
            {'8', '8'},
            {'9', '6'}
        };
        
        std::string rotated = "";
        
        // Process digits in reverse order (simulate 180-degree rotation)
        for (auto it = str_n.rbegin(); it!= str_n.rend(); ++it) {
            char ch = *it;
            // If digit is invalid, return false immediately
            if (rotate_map.find(ch) == rotate_map.end()) {
                return false;
            }
            rotated.push_back(rotate_map[ch]);
        }
        
        // Check if the rotated number is different from the original
        return rotated!= str_n;
    }
};