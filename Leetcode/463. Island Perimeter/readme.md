# Algorithm Idea

Find the start point (the first plot of land) and start a BFS in its adjacent plots, for each plot count the adjacent water, the sum of adjacent water is the perimeter.

# Complexity

- Time: O(n^2) (worst case), O(e+v) + k average case, were k is the iterations to find the start point.

- Space:O(1)

# Results

Python)

- Runtime: 644 ms, faster than 51.07% of Python3 online submissions for Island Perimeter.

- Memory Usage: 16.4 MB, less than 15.71% of Python3 online submissions for Island Perimeter.
