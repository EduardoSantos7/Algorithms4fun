# Algorithm Idea

Create two counter for moves left and right. Count the number of ones and sum up their index and assign it to the counter of moves in right. Also create 2 counters for the number of ones left and right. Iterate the string, in each iteration append the sum of the counter left and right, and if the char in the current iteration is '1' then increase the counter of one left and decrease the counter in right. Sum one left to the counte rof moves in left and decrease the number of ones to the move of rights

# Complexity

- Time: O(n)

- Space:O(n) // Output array

# Results

Runtime
83 ms
Beats
67.98%
Memory
16.8 MB
Beats
7.35%