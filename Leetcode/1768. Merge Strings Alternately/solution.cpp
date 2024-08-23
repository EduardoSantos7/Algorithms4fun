class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        result.reserve(word1.size() + word2.size());
        int min_len = min(word1.size(), word2.size()), i = 0;

        while (i < min_len)
        {
            result += word1[i];
            result += word2[i];
            i++;
        }

        result += (word1.size() > word2.size()) ? word1.substr(i) : word2.substr(i);

        return result;
    }
};
