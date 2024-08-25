class Solution {
public:
    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        return strToInt(firstWord) + strToInt(secondWord) == strToInt(targetWord);
    }

    int strToInt(string word) {
        int decimals = 1; int result = 0;

        for(int i = word.size() - 1; i >= 0; i--) {
            result += decimals * ((int)word[i] - 97);
            decimals *= 10;
        }

        return result;
    }
};