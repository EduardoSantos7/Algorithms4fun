# Algorithm Idea

There're 2 cases when both strings are the same in that casse we should check that a swap is possible, we can create a set to check if there is at least  1 character duplicated. 

The second case in when the strings are different in that case we can check if the pairs (A[i] and B[i]) are the same, if not then store them in an array if thhe array has more than 2 pairss then return false because at the end the array should have only 2 pairs that equivalents.

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Python)

- Runtime: 24 ms, faster than 96.74% of Python3 online submissions for Buddy Strings.

- Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Buddy Strings.