# Algorithm Idea

Build an array of the number of ways to make change for all amounts between 0 and n inclusive. Note that there is only one way to make change for 0: that is to not use any coins. Build up the array one coin denomination at a time. In other words, find the number of ways to make change for all amounts between 0 and n with only one denomination, then with two, etc., until you use all denominations.

# Complexity

- Time: O(Nd) -> where N es the range from 0 to n and d are the denominations

- Space:O(N)

# Results

