# Algorithm Idea

Consider a set/list of only the X coordinate of the points.
Sort it.
Iterate them from the first till the previous to the last and compare each difference between the next value and current value
Check if it's the bigger different seen so far.
Return the biggest different found.

# Complexity

- Time: O(N*LogN)

- Space:O(LogN)

# Results

Runtime
648
ms
Beats
97.51%
of users with Python3
Memory
58.57
MB
Beats
82.22%
of users with Python3