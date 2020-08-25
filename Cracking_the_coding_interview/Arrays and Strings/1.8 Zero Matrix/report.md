# Problem

Write an algorithm such that if an element in an M x N matrix is zero, its entire row and column are set 0.

# Algorithm Idea

**Note**

    - We cannot set to 0 all the column and the row when we found a zero because we will be changing a lot of numbers to 0 and we will finish with a matriz full by zeros.

Approach 1)

    Save the columns and rows where the zeros are located in the first iteration and after that traverse those list setting to zero the specfic rows and columns

Approachh 2)

    Check and save if the first row and col has zeros. Use the first col and row to keep track if a row or col has a zero, then set to zero those columns and rows. Nullify thhe first row and col if they had zeros.

# Complexity

Approach 1)

- Time: O(n \* m)

- Space:O(z) z is the number of zeross

Approach 2)

- Time: O(n \* m)

- Space:O(1)
