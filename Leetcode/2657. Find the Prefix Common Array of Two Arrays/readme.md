# Algorithm Idea

Create two sets, one per every array received as input, init a counter to 0, execute a loop from 0 to n where n is the length of both arrays in the input. For every iteration add the A[i] element in the set and check if it's present in set of b if so increase the counter by one, repeat for b, and append the result into an answer array. 

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
108
ms
Beats
83.40%
of users with Python3

Memory
16.54
MB
Beats
85.68%
of users with Python3