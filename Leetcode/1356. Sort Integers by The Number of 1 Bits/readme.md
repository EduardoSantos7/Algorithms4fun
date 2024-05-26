# Algorithm Idea

Use the  Brian Kerninghan's Algorithm. To find the count of set bits.

Define a function findWeight that takes an integer num and returns its hamming weight using Brian Kerninghan's algorithm.
Initialize weight = 0
While num > 0:
Increment weight
Set num to num & (num - 1)
Return weight
Create a custom comparator with findWeight. Sort arr with the custom comparator.
Return arr.

# Complexity

- Time: O(nlogn)

- Space:O(logn)

# Results

Runtime
59
ms
Beats
65.33%
of users with Python3

Memory
16.76
MB
Beats
44.95%
of users with Python3