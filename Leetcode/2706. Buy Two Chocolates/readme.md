# Algorithm Idea

Approach 1)

Sort the array and if the sum of the first 2 elements are smaller than the money received as param then return the difference if not return money.

Approach 2)

Find the two minimum in one pass and if their sum is smaller than the money received as param then return the difference if not return money.

# Complexity

Approach 1)

- Time: O(NLogN)
-  Space:O(N)
  
Approach 2)

- Time: O(N)
- Space:O(1)

Note: for smaller N like in this problem, NlogN will be better than N

# Results

Approach 1)

Rust)

Runtime
0
ms
Beats
100.00%

Memory
2.07
MB
Beats
86.84%

Python)

Runtime
56
ms
Beats
74.41%

Memory
16.58
MB
Beats
37.82%

Approach 2)

Rust)

Runtime
0
ms
Beats
100.00%

Memory
2.22
MB
Beats
18.42%

Python)

Runtime
67
ms
Beats
15.55%

Memory
16.50
MB
Beats
37.82%