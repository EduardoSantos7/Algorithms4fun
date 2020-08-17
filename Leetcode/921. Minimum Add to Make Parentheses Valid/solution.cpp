class Solution
{
public:
    int minAddToMakeValid(string S)
    {
        vector<int> stack;

        for (int i = 0; i < S.size(); i++)
        {
            if (!stack.empty() && stack.back() == '(' && S[i] == ')')
            {
                stack.pop_back();
            }
            else
            {
                stack.push_back(S[i]);
            }
        }

        return stack.size();
    }
};