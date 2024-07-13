# Algorithm Idea

Approach 1)

Sort the array, find the common difference substracting the sond element and the first.
Iterate the array and verify all the elements have the same difference with their antecesor.

Approach 2)

Find the two minimum values in one pass.
Create a hashset to check the existence of elements later
Iterate from 0 to the array length, checking if the expected number in that position is in the set if not return false, if all the elements expected are in the set return true.

Note: the main difference in those approaches if how to get the minimum difference and validate that difference for all the elements, while sorting make it more easy it increases the complexity. Also take care of cases with duplicates.

# Complexity

Approach 1)

- Time: O(NLogN)

- Space:O(N)

Approach 2)

- Time: O(N)

- Space:O(N)

# Results

Approach 1)

Runtime
1
ms
Beats
75.00%

Memory
2.07
MB
Beats
92.86%

Approach 2)

Runtime
1
ms
Beats
75.00%

Memory
2.09
MB
Beats
92.86%