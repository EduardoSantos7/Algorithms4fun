class Solution {
public:
    int removePalindromeSub(string s) {
        int p1 = 0; int p2 = s.size() - 1;
        while (p1 < p2) {
            if (s[p1] != s[p2]) { return 2; }
            p1++; p2--;
        }
        return 1;
    }
};