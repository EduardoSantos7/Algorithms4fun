# Problem

Assume you have a method isSubstring which checks if one world is a substring of another. Given 2 strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

# Algorithm Idea

concatenate the base string with itself aand check if the second string is a substring

# Complexity

- Time: O(N) asumming that isSubstring is (A + B)

- Space:O(1)
