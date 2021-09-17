# Algorithm Idea

Create an array of size: n+1, the first element in the array will be 0, and the iteration will be from 1 to n+1, in each iteration you should check if the current i is the same as 2 times the previous multiple of 2, if that's the cas eupdate the previous multiple to i. in the location i in the answer array you will add the number in (the previous multiple of 2 position minus i) + 1.

# Complexity

- Time: O(N)

- Space:O(N)

# Results

Python)

- Runtime: 80 ms, faster than 82.52% of Python3 online submissions for Counting Bits.
- 
- Memory Usage: 20.9 MB, less than 35.50% of Python3 online submissions for Counting Bits.
