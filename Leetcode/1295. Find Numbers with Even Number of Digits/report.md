# Algorithm Idea

For each number in the list the script will count the digits in it dividing the number by then while it is greater than 0. That's enough but adding a dictionary of seen number we can increase the speed.

# Complexity

**Basic Algorithm:**

    - Time: O(n*s) where s is the sum of all the digits and n is the length oof the list
    - Space:O(1)

**Using a Dictionary:**

    - Time: O(m*j) where m is the subset of the numbers withouth duplicates and j the sum of its digits
    - Space: O(n)

# Results

**Basic Algorithm:**

    1) Python:

        - Runtime: 60 ms, faster than 15.06% of Python3 online submissions for Find Numbers with Even Number of Digits.
        - Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
    
    2) Go:

        - Runtime: 4 ms, faster than 87.58% of Go online submissions for Find Numbers with Even Number of Digits.
        - Memory Usage: 3.1 MB, less than 100.00% of Go online submissions for Find Numbers with Even Number of Digits.

**Using a Dictionary:**

    1) Python:

        - Runtime: 44 ms, faster than 97.77% of Python3 online submissions for Find Numbers with Even Number of Digits.

        - Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.

    2) Go:

        - Runtime: 4 ms, faster than 87.58% of Go online submissions for Find Numbers with Even Number of Digits.
        - Memory Usage: 3.1 MB, less than 100.00% of Go online submissions for Find Numbers with Even Number of Digits.