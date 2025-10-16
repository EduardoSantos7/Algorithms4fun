# Algorithm Idea

Approach 1)

Use a flag to know where evaluate for +1 or -1, this evaluation is perform constanly in a while loop while an outside for loop guide the start point

Approach 2)

Use a while loop to move i where the start of +1 is met and in that case use an inner while loop to evaluate the expected value, when it finish set the i to the last element checked.

# Complexity

Approach 1)

- Time: O(N*N)

- Space:O(1)

Approach 2)

- Time: O(N)

- Space:O(1)

# Results

Approach 1)

Runtime

51
ms
Beats
9.01%

Memory
17.85
MB
Beats
51.07%


Approach 2)

Runtime

8
ms
Beats
56.22%

Memory
17.93
MB
Beats
33.48%
