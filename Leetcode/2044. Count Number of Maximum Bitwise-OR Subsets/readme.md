# Algorithm Idea

Approach 1)

Idea: Generate all subsets recursively. For each number, either include it in the subset or exclude it. Count subsets where the OR value equals the maximum OR value.
Key Insight: Use recursion to explore all 2^n subsets, summing valid subsets.

Approach 2)

Idea: Optimize recursion by storing results of overlapping sub-problems. Use a 2D memo table to save results based on the current index and OR value.
Key Insight: Avoid recomputing results for the same state (index and OR value).

Approach 3)

Idea: Represent each subset using a bitmask (integer). Iterate over all possible subsets (bitmasks), compute their OR values, and count subsets achieving the maximum OR value.
Key Insight: Use binary representation of integers to enumerate subsets efficiently.

Approach 4)

Idea: Use a dp array where dp[i] represents the count of subsets with OR value i. For each number in nums, update dp to reflect new subsets formed by OR-ing the number with existing subsets.
Key Insight: Mimics the knapsack problem by dynamically updating possible OR values.

# Complexity

Approach 1)

- Time: O(2^N)

- Space:O(N)

Approach 2)

- Time: O(N*maxOrValue)

- Space:O(N*maxOrValue)

Approach 3)

- Time: O(2^N * N)

- Space:O(1)

Approach 4)

- Time: O(N*maxOrValue)

- Space:O(2^17)

# Results

Approach 1)

Runtime
219
ms
Beats
66.27%

Memory
16.61
MB
Beats
68.80%

Approach 2)

untime
407
ms
Beats
28.52%

Memory
32.73
MB
Beats
6.01%

Approach 3)

Runtime
1274
ms
Beats
14.26%

Memory
16.60
MB
Beats
90.20%

Approach 4)

Runtime
2824
ms
Beats
5.03%

Memory
17.32
MB
Beats
23.44%