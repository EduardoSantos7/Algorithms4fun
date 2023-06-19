# Algorithm Idea

First of all, we build a counter table out of the given list of numbers.

We would then use this counter table during our backtracking process, which we define as the function backtrack(comb, remain, curr, candidate_groups, results).
In order to keep the state of each backtracking step, we use quite a few parameters in the function, which we elaborate as follows:

comb: the combination we built so far at each step.
remain: the remaining sum that we need to fill, in order to reach the target sum.
curr: the cursor that points to the current group of number that we are using from the counter table.
counter: the current counter table.
results: the final combinations that have the target sum.
At each invocation of the backtracking function, we first check if we reach the target sum (i.e. sum(comb) = target), and if we should stop the exploration simply because the sum of current combination goes beyond the desired target.

If there is still some remaining sum to fill, we will then iterate through the current counter table to pick the next candidate.

Once we pick a candidate, we then continue the exploration by invocating the backtrack() function with the updated states.
More importantly, at the end of each exploration, we need to revert the state we updated before, in order to start off a clean slate for the next exploration.

# Complexity

- Time: O(2^n)

- Space:O(n)

# Results

Runtime
74 ms
Beats
74.71%
Memory
16.5 MB
Beats
13.48%