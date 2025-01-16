# Algorithm Idea

we consumed numExchange bottles in each iteration. By using math operations, we can do this more efficiently. We can consume numExchange * K bottles in one go, where K is the largest integer such that numExchange * K < numBottles. K is calculated as integer division numBottles / numExchange. After consuming numExchange * K bottles, we exchange them for K full bottles (one for each set of numExchange empty bottles).

# Complexity

- Time: O(Log(N))

- Space:O(1)

# Results

Runtime
38
ms
Beats
27.62%

Memory
16.63
MB
Beats
6.67%