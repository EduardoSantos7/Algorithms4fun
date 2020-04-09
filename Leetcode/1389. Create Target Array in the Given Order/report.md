# Algorithm Idea

Iterate at the same time the index and nums arrays and just insert tthe value in the correct position in the result list. In Go is the same idea but there is not a function insert insted we need to create an extra spot, shift the elements and assign the new one.

# Complexity

- Time: O(n^2) -> insert() complexity is o(n)
- Space:O(1)

# Results

1) Python:

    - Runtime: 28 ms, faster than 90.44% of Python3 online submissions for Create Target Array in the Given Order.

    - Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.

2) Go:

    - Runtime: 0 ms, faster than 100.00% of Go online submissions for Create Target Array in the Given Order.

    - Memory Usage: 2.1 MB, less than 100.00% of Go online submissions for Create Target Array in the Given Order.
