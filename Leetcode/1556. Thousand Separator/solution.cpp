class Solution {
public:
    string thousandSeparator(int n) {
        if(n < 1000)
        {
            return  to_string(n);
        }

        string result = to_string(n);
        int count = 0;

        for(int i = result.size() - 1; i >= 0; i--)
        {
            count++;
            if(count % 4 == 0)
            {
                result.insert(i + 1, ".");
                count = 1;
            }
        }

        return result;
    }
};