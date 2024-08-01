# Algorithm Idea

Get what should be the base (length - 1)
Check if the last element is the same as the base, if not return false
Iterate the array from 0 to the base. Check if the current number in the array is the same as the number it should be (i + 1) if not return false.
If you finish to iterate all the numbers without return, then return true.

# Complexity

- Time: O(NLogN)

- Space:O(1)

# Results

Runtime
50
ms
Beats
47.38%

Memory
16.56
MB
Beats
40.97%