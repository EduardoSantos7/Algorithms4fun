# Problem

There are 3 types of edits tthat canbe perfoormed on strings: insert, remove and repllace a char. Given 2 sttrings, write a function to ccheck if they are one edit or zero away.

# Algorithm Idea

We can compare the lengths of both strings if the diference is more than 1 we can return false directly. If not then we can use 2 pointers to move across both strings and count the diferences. We shhoulld know which is the smallest string

# Complexity

- Time: O(N) the length of the smallest string

- Space:O(1)
