#include <string>
#include <array>
#include <set>
#include <cctype>
#include <algorithm>

class Solution {
    public:
        std::string longestNiceSubstring(std::string s) {
            auto [start, end] = longestNiceSubstring(s, 0, s.size());
            return s.substr(start, end - start);
        }

    private:
        [[nodiscard]] std::array<int, 2> longestNiceSubstring(const std::string& s, int left, int right) {
            auto charSet = [&s, left, right] {
                std::set<char> result;
                for (int i = left; i < right; ++i) {
                    result.insert(s[i]);
                }
                return result;
            }();

            for (int i = left; i < right; ++i) {
                char lower = std::tolower(s[i]);
                char upper = std::toupper(s[i]);

                if (!charSet.count(lower) || !charSet.count(upper)) {
                    auto prefix = longestNiceSubstring(s, left, i);
                    auto suffix = longestNiceSubstring(s, i + 1, right);

                    return (prefix[1] - prefix[0] >= suffix[1] - suffix[0]) ? prefix : suffix;
                }
            }

            return {left, right};
        }
};
