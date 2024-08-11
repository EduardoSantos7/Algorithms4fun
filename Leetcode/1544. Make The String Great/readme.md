# Algorithm Idea

Approach 1)

Iterate the string with two pointers with an offset of 1 to check if the absolute difference in between both letters are exactly 32 in that case then you remove them from the string and star again.

Approach 2)

Use an stack to keep track of all the chars in the string, if the last one has an absolute difference of 32 with the current char then pop it from the stack. Otherwise add it to the stack and at the end concatenate the stack to form a string.

# Complexity

Approach 1)

- Time: O(N)

- Space:O(N)

Approach 2)

- Time: O(N)

- Space:O(N)

# Results

Approach 1)

Runtime
37
ms
Beats
63.23%

Memory
16.54
MB
Beats
25.30%

Approach 2)

Runtime
42
ms
Beats
28.17%

Memory
16.44
MB
Beats
65.90%