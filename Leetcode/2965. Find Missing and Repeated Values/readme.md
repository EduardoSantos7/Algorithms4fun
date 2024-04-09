# Algorithm Idea
Generate two sets, one with the numbers expected from 1 to n*n +1, and the other one keep it empty.
Create an array of integers of size 2 called res.
Iterate the grid, for each value in the cell check if it's a seen number, in that case set the first cell of the res array to this value.
If you haven't seen it then remove it from expected numbers and add it to seen.
After finish to iterate the grid set the second cell f the res array to the only element left in expected numbers set.
return res array.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
117
ms
Beats
67.08%
of users with Python3
Memory
17.19
MB
Beats
16.08%
of users with Python3