#include <cstring>

class Solution {
public:
    string modifyString(string s) {
        for (int i = 0; i < s.length(); ++i)
        {
            if (s[i] == '?')
            {
                for (char c = 'a'; c <= 'c'; ++c)
                {
                    if ((i > 0 && s[i-1] == c) || (i < s.length() - 1 && s[i+1] == c)) {
                        continue;
                    }
                    s[i] = c;
                    break;
                }
            }
        }

        return s;
    }
};