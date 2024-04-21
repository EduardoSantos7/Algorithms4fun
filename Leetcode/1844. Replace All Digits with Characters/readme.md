# Algorithm Idea

Create an array with all the chars of the string in it.
Iterate the array starting from one to the last element of the array, by step of 2.
Set a new value for the current position by:
 - converting the previous position to its ASCII representation
 - Sum up the integer value of the current char
 - Cast the new number into its ASCII representation
Return the concatenation of th array as string.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
39
ms
Beats
29.45%
of users with Python3
Memory
16.55
MB
Beats
44.92%
of users with Python3