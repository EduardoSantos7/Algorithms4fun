# Algorithm Idea
Use 3 variables to track the past 3 computation and iterate n - 3 time swapping these values. Finally, the last variable stores our result. In this approach, we should verify if n < 3.

Other approaches include an array to store all the values or recursion.

# Complexity
Time: O(n)
Space:O(1)

# Results
Runtime: 20 ms, faster than 98.78% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for N-th Tribonacci Number.