#include <vector>
#include <string>
#include <cctype>  // For std::isdigit

using namespace std;

class Solution {
public:
    string reformatNumber(string number) {
        // Step 1: Extract only digit characters
        string digits;
        for (char ch : number) {
            if (isdigit(ch)) {
                digits.push_back(ch);
            }
        }

        // Step 2: Format the extracted digits
        string formatted;
        int i = 0;
        int n = digits.length();
        
        // Process chunks of 3 until less than 4 digits remain
        while (n - i > 4) {
            formatted.append(digits.substr(i, 3) + "-");
            i += 3;
        }
        
        // Process the final 4 or fewer digits
        if (n - i == 4) {  // If 4 digits remain, split them into 2-2
            formatted.append(digits.substr(i, 2) + "-" + digits.substr(i + 2, 2));
        } else {  // For 3 or fewer digits, just append them
            formatted.append(digits.substr(i));
        }

        return formatted;
    }
};
