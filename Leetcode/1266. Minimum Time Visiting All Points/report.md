# Algorithm Idea

The total time is the sum of each transition time, the transition time is
the max between the absolute difference in X and the absolute difference in Y.

Ex:

[[3,2],[-2,2]] -> X dif = abs(3 - -2) = 5, Y dif = abs(2 - 2) = 0 ;


# Complexity

- Time: O(n)

- Space:O(1)

# Results

- Python:

    - Runtime: 56 ms, faster than 83.94% of Python3 online submissions for Minimum Time Visiting All Points.

    - Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.

- Go:

    - Runtime: 4 ms, faster than 89.09% of Go online submissions for Minimum Time Visiting All Points.

    - Memory Usage: 3.4 MB, less than 100.00% of Go online submissions for Minimum Time Visiting All Points.