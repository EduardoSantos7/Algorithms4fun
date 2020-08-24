# Problem

Write a method to replace all the spaces in a string with `%20`. You might assume that the string has suffienctt space at the end to hold the additional chars, and that you're given the `true` length oof the string.

# Algorithm Idea

Traverse the string and store the current char in a list if the char is not a space if so save a `%20` at the end join the list.

**Note:**

- In other languages like C is useful to have the space at the end of the question as the problem mention because strings are unmutable but we can `rebuild` the string from the end. I think this is not necesary due to python.

# Complexity

- Time: O(N)

- Space:O(N)
