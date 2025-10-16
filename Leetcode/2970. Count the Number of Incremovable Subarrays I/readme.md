# Algorithm Idea

The problem can be approached by decomposing the array into three regions: a prefix, a suffix, and a middle segment. Removing one contiguous block corresponds to keeping either:

A prefix (by removing a suffix),
A suffix (by removing a prefix), or
Both a prefix and a suffix with a middle segment removed between them.
The objective is to count all such removals that leave the remaining array strictly increasing. The analysis must also account for the special case where the array is already strictly increasing.

return res array.

# Complexity

- Time: O(n^2)

- Space:O(1)

# Results

Runtime
0
ms
Beats
100.00%

Memory
17.78
MB
Beats
54.32%
