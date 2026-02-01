# Algorithm Idea

For each element, we need to find the number of rounds it will take for it to be removed. The answer is the maximum number of rounds for all elements. Build an array dp to hold this information where the answer is the maximum value of dp.

Use a stack of the indices. While processing element nums[i], remove from the stack all the indices of elements that are smaller than nums[i]. dp[i] should be set to the maximum of dp[i] + 1 and dp[removed index].

# Complexity

- Time: O(N)

- Space:O(N)

# Results

Runtime
169
ms
Beats
67.37%

Memory
32.88
MB
Beats
75.00%