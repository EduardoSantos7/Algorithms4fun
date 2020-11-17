# Algorithm Idea

We know the array arr should end up like expect = sorted(arr). If the count of the first k elements minus the count what those elements should be is zero everywhere, then the first k elements form a valid chunk. We repeatedly perform this process.

We can use a variable nonzero to count the number of letters where the current count is non-zero.

# Complexity

- Time: O(NlogN)

- Space:O(N)

# Results

- Runtime: 60 ms, faster than 99.24% of Python3 online submissions for Max Chunks To Make Sorted II.

- Memory Usage: 14.6 MB, less than 12.21% of Python3 online submissions for Max Chunks To Make Sorted II.