# Algorithm Idea

1) Brute Force

    Traverse the lliist from 0 to N-2 and get the max element in the sub list in the right each time.

2) Optimized

    The worst part of the brute force approach is that we are computing the max in each time.

    Ex.

    [1,5,7,9,60,10]

    For 1, 5, 7 and 9 the max in the right list is always 60 but we are calculate it 4 times.

    This approach only calculate the new max when we are in the max position. The complixity could
    be the same but the number of computation is smaller.

# Complexity

1) Brute Force

    - Time: O(n^2)
    - Space:O(1)

1) Brute Force

    - Time: O(n^2)
    - Space:O(1)

# Results

1) Brute Force

    a) Python

        - Runtime: 4668 ms, faster than 23.10% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.

        - Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
    
    b) Go

        - Runtime: 144 ms, faster than 24.10% of Go online submissions for Replace Elements with Greatest Element on Right Side.

        - Memory Usage: 6 MB, less than 100.00% of Go online submissions for Replace Elements with Greatest Element on Right Side.

2) Optimized

    a) Python

        - Runtime: 120 ms, faster than 96.10% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.

        - Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
    
    b) Go

        - Runtime: 16 ms, faster than 76.51% of Go online submissions for Replace Elements with Greatest Element on Right Side.

        - Memory Usage: 6.1 MB, less than 100.00% of Go online submissions for Replace Elements with Greatest Element on Right Side.
