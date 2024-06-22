# Algorithm Idea

Approach 1)

Convert the integer to a binary string.
If there is only one bit return True
Iterate from the second bit to the last comparing if the previous bit is different.
If it's different continue else return False
If you finish to iterate return True

Approach 2)

Bits logic

Approach 3)

Convert the integer to a binary string.
If there is only one bit return True
Check if the substrings "00" or "11" are present in the binary string

# Complexity

Approach 1)

- Time: O(n)

- Space:O(1)

Approach 2)

- Time: O(1)

- Space:O(1)

Approach 3)

- Time: O(n)

- Space:O(1)

# Results

Approach 1)

Runtime
33
ms
Beats
69.04%
of users with Python3

Memory
16.49
MB
Beats
86.22%
of users with Python3

Approach 2)

Runtime
33
ms
Beats
69.04%
of users with Python3

Memory
16.58
MB
Beats
34.22%
of users with Python3

Approach 3)

Runtime
38
ms
Beats
31.80%
of users with Python3

Memory
16.55
MB
Beats
34.22%
of users with Python3