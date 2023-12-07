class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0;
        bool result = false;

        while( i < bits.size()) {
            if (bits[i] == 0)
            {
                result = true;
                i += 1;
                continue;
            }

            result = false;
            i += 2;
        }

        return result;
    }
};