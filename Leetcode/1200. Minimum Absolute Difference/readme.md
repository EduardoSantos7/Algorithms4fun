# Algorithm Idea

Approach 1) (Brute force)

Sort the array. Find the minimum absolute differencee. Use the array to create a set. Iterate the array and find in the set the numbers needed to create a correct pair and insert.

Approach 2)

Sort the array. Iterate the array and get the difference between the current number and previous one. If it's the same as the current minimum difference then insert the pair. If the difference is smaller then clear the pairs so far and update the minimum difference.

# Complexity

- Time: O(nlogn)

- Space:O(n)

# Results

Approach 1)

Python)

- Runtime: 388 ms, faster than 26.85% of Python3 online submissions for Minimum Absolute Difference.

- Memory Usage: 32.2 MB, less than 14.57% of Python3 online submissions for Minimum Absolute Difference.

Approach 2)

Python)

- Runtime: 328 ms, faster than 83.37% of Python3 online submissions for Minimum Absolute Difference.

- Memory Usage: 28.2 MB, less than 25.54% of Python3 online submissions for Minimum Absolute Difference.
