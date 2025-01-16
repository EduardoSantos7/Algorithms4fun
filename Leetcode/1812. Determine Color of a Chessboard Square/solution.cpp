class Solution {
public:
    bool squareIsWhite(string coordinates) {
        std::map<char, bool> flags = {
            {'a', false}, {'b', true}, {'c', false}, {'d', true},
            {'e', false}, {'f', true}, {'g', false}, {'h', true}
        };

        bool even = ((coordinates[1] - '0') % 2) == 0;

        if (flags[coordinates[0]] && even) {
            return false;
        }
        else if (flags[coordinates[0]] && !even) {
            return true;
        }
        else if (!flags[coordinates[0]] && even) {
            return true;
        }
        else {
            return false;
        }
    }
};