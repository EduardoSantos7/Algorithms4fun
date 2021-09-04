# Algorithm Idea

Approach 1)

Cast from list to a str, cast to int, add the number k, cast to str and cast it to a list.

Approach 2)

Iter the array from the last element and add the equivalent k number, keep an acum for a result bigger than 9. After finish to iterate if you still have a k and acum add it to the number in the beggining.

# Complexity

Approach 1)

- Time: O(n)

- Space:O(n)

Approach 2)

- Time: O(n)

- Space:O(1)

# Results

Approach 1)

Python)

- Runtime: 423 ms, faster than 24.00% of Python3 online submissions for Add to Array-Form of Integer.

- Memory Usage: 15.1 MB, less than 75.41% of Python3 online submissions for Add to Array-Form of Integer.

Approach 2)

Python)

- Runtime: 276 ms, faster than 90.73% of Python3 online submissions for Add to Array-Form of Integer.

- Memory Usage: 15.3 MB, less than 34.80% of Python3 online submissions for Add to Array-Form of Integer.

Rust)

- Runtime: 12 ms, faster than 100.00% of Rust online submissions for Add to Array-Form of Integer.

- Memory Usage: 2.1 MB, less than 100.00% of Rust online submissions for Add to Array-Form of Integer.
