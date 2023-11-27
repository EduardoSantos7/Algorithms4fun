class Solution {
    public:
        bool isAcronym(vector<string>& words, string s) {
            std::string initials;
            for (const auto& word : words) {
                initials += word.front();
            }
            return initials == s;
        }
};