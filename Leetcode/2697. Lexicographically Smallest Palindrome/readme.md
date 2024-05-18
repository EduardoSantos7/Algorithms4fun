# Algorithm Idea

Use two pointers, one starts at 0 and the other one at the index of the last character.

While the pointer that start from the left is smaller or equal to the one in the right, check the character in the position of the pointer in the left is smaller that the char in in the right, in that case make the right one the same as the left else make them both equals to the one in the right.

Increase the counter in the left by one and decrease the one in the right by 1.

return the new string.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
89
ms
Beats
94.03%
of users with Python3

Memory
16.67
MB
Beats
85.66%
of users with Python3