# Algorithm Idea

Init a counter.
For each log in logs check:
- If it's equals to "../" and the counter is bigger than zero, in that case decrease the counter by 1.
- If the beginning of the log is not a point ".", in that case increase the counter by 1.
Return the counter after iterate all the logs.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
47
ms
Beats
70.80%
of users with Python3

Memory
16.78
MB
Beats
63.09%
of users with Python3