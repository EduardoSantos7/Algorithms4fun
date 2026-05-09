# Algorithm Idea

Approach 1)

For every cell, check the full horizontal and vertical run passing through that cell. If the run has 3 or more equal non-zero candies, add those positions to a target set. After scanning the whole board, crush all target cells simultaneously by setting them to `0`, then apply gravity column by column. Repeat until no more candies can be crushed.

Approach 2)

Scan each row and each column using run detection. Instead of checking the full horizontal/vertical path from every cell, detect each continuous run once. If a run has 3 or more equal non-zero candies, mark those cells as negative. After all horizontal and vertical runs are marked, apply gravity by moving only positive candies downward and filling the top with `0`. Repeat until no more candies can be crushed.

# Complexity

Approach 1)

- Time: O(K * M * N * (M + N))
- Space: O(M * N)

Approach 2)

- Time: O(K * M * N)
- Space: O(1)

Where:

- `M` = number of rows
- `N` = number of columns
- `K` = number of crush/gravity rounds until the board becomes stable

Note: The worst-case upper bound can be written as O((M * N)^2) for Approach 2 because each successful round crushes at least 3 candies. However, the more practical expression is O(K * M * N).

# Difference Between Approaches

Approach 1 works, but it repeats a lot of scanning. For every cell, it may scan left/right and up/down again, even if those candies were already part of a run checked from another cell.

Approach 2 is better because it scans each row and each column directly and detects each run once. It also avoids storing a separate target set by marking candies in-place using negative values.

Using NumPy can make this even faster in practice because NumPy performs board-wide comparisons in optimized native code instead of Python loops. However, the Big-O complexity is still O(K * M * N), and NumPy uses extra memory for arrays/masks. In interviews, the non-NumPy version is usually better because it shows the algorithm clearly and does not depend on external libraries.

# Results

Approach 1)

Python)

Runtime  
100 ms  
Beats  
9.62%

Memory  
19.50 MB  
Beats  
48.11%

Approach 2)

Python)

Runtime  
39 ms  
Beats  
91.57%

Memory  
19.32 MB  
Beats  
81.51%