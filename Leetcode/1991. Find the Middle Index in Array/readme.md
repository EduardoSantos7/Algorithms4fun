# Algorithm Idea

Approach 1)

Create to array to store the pre compute sum for each side (right and left).
Get the pre sum for each position and append it in its array.
Iterate from 0 to n and check if the item in that position for both array is the same in that case return the index.
If hasn't return then return -1/

Approach 2)

Using a variable to get the sum of all the elements from the right.
Iterate from 0 to n and decrease the right sum by the current number, and increase the left sum by the previous number (if you are at the index 0 the sum is 0).
Then check if both left and right sum are the same. In that case return i.
If at the end of the iteration you haven't returned then return -1.


# Complexity

Approach 1)

- Time: O(N)

- Space:O(N)

Approach 2)

- Time: O(N)

- Space:O(1)

# Results

Approach 1)

Runtime
40
ms
Beats
71.38%

Memory
16.62
MB
Beats
35.59%

Approach 2)

Runtime
35
ms
Beats
92.30%

Memory
16.57
MB
Beats
35.59%