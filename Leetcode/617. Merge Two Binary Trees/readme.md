# Algorithm Idea

Using a recursive dfs to modify in place one of the trees, in each iteration traverse both trees at the same time and sum up the values in case both are different from null, check for the trees below the current node to verify we don't need to update.

# Complexity

- Time: O(m) - where m is the number of nodes in one of the trees

- Space:O(m) - due to recursion

# Results

Python)

- Runtime: 84 ms, faster than 82.86% of Python3 online submissions for Merge Two Binary Trees.

- Memory Usage: 15.3 MB, less than 92.30% of Python3 online submissions for Merge Two Binary Trees.
