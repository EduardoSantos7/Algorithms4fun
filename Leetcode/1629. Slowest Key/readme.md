# Algorithm Idea

In one iteration we can calculate the slowest key by checking the current released time and compare it with a current max. We should also update the key at the same time if the time is bigger than max or if it's equal and the current key is bigger than preevious one.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
51
ms
Beats
79.72%
of users with Python3

Memory
16.75
MB
Beats
50.23%
of users with Python3