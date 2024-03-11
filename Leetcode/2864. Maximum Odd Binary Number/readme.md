# Algorithm Idea

To solve this problem with only one O(n)O(n)O(n) pass, let's first focus on rearranging all bits such that all 1 bits come before all 0 bits in string s. Consider the two ends of string s, referenced by the pointers left and right. Keep moving the left pointer to the right until it reaches a 0 bit, and keep moving the right pointer to the left until it reaches a 1 bit. If both conditions are met when the left pointer is less than the right pointer, we can swap these two bits and continue with the two pointers process.

This works because the left pointer will only move when all bits that precede it are all 1 bits, and similarly for the right pointer. This algorithm is also guaranteed to terminate, since at every step, at least one pointer will iterate.

When this two pointers process is done, the left pointer is next to the rightmost occurence of a 1 bit in the rearranged s. The last step is to swap this 1 bit with the last position in s to ensure the resulting string is odd.


# Complexity

- Time: O(n)

- Space:O(n)

# Results
Runtime
47
ms
Beats
8.25%
of users with Python3
Memory
16.54
MB
Beats
62.74%
of users with Python3