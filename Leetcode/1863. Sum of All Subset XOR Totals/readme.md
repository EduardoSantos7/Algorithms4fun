# Algorithm Idea

Initialize a variable result to 0.
For each num in nums:
Take the running OR of result and num, result |= num.
Append N - 1 zeros to the right of the binary representation of result by shifting result by N - 1 places, result << (N - 1).

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Runtime
39
ms
Beats
81.83%

Memory
16.42
MB
Beats
64.29%