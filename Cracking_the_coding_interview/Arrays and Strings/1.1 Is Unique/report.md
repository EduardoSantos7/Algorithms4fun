# Problem

Implement an algo. to determine if a string has all unique chars. What if you cannot use additional data structure?

# Algorithm Idea

Check if the char in a set, if it is then return false, iterate all chars and if you haven't finish return true.

Other approach is assuming the chars are ascii we can use an integer (8 bits) to check for duplicates.

**What if you cannot use additional data structure?**

2 approaches are: 1) to check each char in the string next to the char. O(n^2) 2) sort the string and check for duplicates in the char next to the current one.

# Complexity

- Time: O(N)

- Space:O(c) C is the length of the set of unique chars, we can use an array and assume that the array hass a len of 128 for ascii chars and say thatt the space complexity is constant.
