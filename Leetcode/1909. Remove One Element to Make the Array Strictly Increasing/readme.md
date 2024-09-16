# Algorithm Idea

Iterate the array from the second index.
For each number check if it's strictly bigger than the previous one.
In that case then just assign a variable called last_good to the current number.
But if it's not check if a flag bad_number is already set in that case return False.
If hasn't been set then set it and if it's the first element or it's bigger than 2 behind then set last good to this value and continue to the next iteration.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
47
ms
Beats
79.56%

Memory
16.60
MB
Beats
63.43%