# Algorithm Idea

Approach 1)

Get the frequencies of each word in both strings received in the params.

return the concatenation of the words in both counters where the value is only 1 and is not present in the other counter

Approach 2)

Declare two sets, one to store the result and the other one to track the seen strings

Split the two string received by space and concatenate it (optional, you can just do two loops)

for each word check if it's not in the set and hasn't been seen before, in that case add it to the set

if the word is in the set remove it from it and add it to seen.

return the set

# Complexity

Approach 1)

- Time: O(n)

- Space:O(n)

Approach 2)

- Time: O(n)

- Space:O(n)

# Results

Approach 1)

Runtime
27
ms
Beats
94.66%
of users with Python3

Memory
16.60
MB
Beats
15.94%
of users with Python3