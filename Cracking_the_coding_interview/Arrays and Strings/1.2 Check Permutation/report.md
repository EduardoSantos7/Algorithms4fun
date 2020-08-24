# Problem

Given 2 strings, write a method to decide if one is a permutation of the other.

**A string is a permutation of another if both has the same chars (probably in diferent index)**

# Algorithm Idea

Iterate the first string using a `hashmap` to count the chars ocurrence and iterate the second one decreasing the count. At the end all the keys should has a value of zero if not then return fase in the other hand you can return false if in the second iteration one char that is not in the hashmap appears.

**Both string must have the same length**

I'm assuming that case matters and any other special char too.

# Complexity

- Time: O(N)

- Space:O(N) where n is the length of the string
