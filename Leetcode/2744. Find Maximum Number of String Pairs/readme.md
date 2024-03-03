# Algorithm Idea

Create 2 sets, one to skip the already checked words and its reverse and the other one to do lookups into the input array of words. Init a count to track the number of pairs. Iterate the list of words, for each word check if you already checked it in that case skip it. If not then init a variable with its reverse and check if the word and its reverse are different and reversed word is in the set for look ups, if so then increase the counter by 1. Return the counter.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
50
ms
Beats
56.85%
of users with Python3

Memory
16.58
MB
Beats
65.37%
of users with Python3