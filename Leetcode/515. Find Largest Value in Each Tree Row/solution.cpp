/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

using namespace std;

class Solution
{
public:
    vector<int> largestValues(TreeNode *root)
    {
        if (root == nullptr)
        {
            return {};
        }
        vector<int> level;
        vector<int> max_in_level;
        vector<TreeNode *> row = {root};

        while (!row.empty())
        {
            for (int i = 0; i < row.size(); i++)
            {
                level.push_back((*row[i]).val);
            }

            max_in_level.push_back(*max_element(level.begin(), level.end()));

            vector<TreeNode *> new_row;

            for (int i = 0; i < row.size(); i++)
            {
                if ((*row[i]).right != nullptr)
                {
                    new_row.push_back((*row[i]).right);
                }
                if ((*row[i]).left != nullptr)
                {
                    new_row.push_back((*row[i]).left);
                }
            }

            row = new_row;
            level = {};
        }

        return max_in_level;
    }
};