class Solution {
public:
    bool halvesAreAlike(string s) {
        int mid = s.length() / 2;
        string first_half = s.substr(0, mid);
        string second_half = s.substr(mid);
        return countVowels(first_half) == countVowels(second_half);
    }

    int countVowels(string s) {
        int res = 0;

        for (int i = 0; i < s.size(); i ++) {
            if (isvowel(s[i])){
                res++;
            }
        }

        return res;
    }

    bool isvowel(char v) {
        return (0x208222>>(v&0x1f))&1;
    }
};