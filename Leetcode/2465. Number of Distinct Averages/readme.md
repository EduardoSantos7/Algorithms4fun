# Algorithm Idea

Sort the numbers,
Use two pointer to get the min and max at the same time.
Compute the average of min and max and check if you have already see it, if not save it.
Increase the pointer to the min and decrease the pointer to the max.
Return the count of average saved.

# Complexity

- Time: O(NLogN)

- Space:O(N)

# Results

Rust)

Runtime
1
ms
Beats
100.00%

Memory
2.49
MB
Beats
50.00%

Python)

Runtime
29
ms
Beats
91.70%

Memory
16.66
MB
Beats
15.24%

Golang)

Runtime
0
ms
Beats
100.00%

Memory
2.21
MB
Beats
70.59%
