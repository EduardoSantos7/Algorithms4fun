# Algorithm Idea

The function first finds the number of zeros to be duplicated and then copies each zero twice and each non-zero once.

The function initializes two variables, possible_dups and length. possible_dups keeps track of the number of zeros to be duplicated, and length is the index of the last element in the vector.
The function then loops through the vector from left to right and counts the number of zeros to be duplicated. If the current element is zero, the function increments possible_dups. If the current element is the last element in the vector, the function sets the last element to zero and decrements length.
The function then calculates the index of the last element in the modified vector by subtracting possible_dups from length.
Finally, the function loops through the vector from right to left and copies each element to its new position. If the current element is zero, the function copies it twice. If the current element is non-zero, the function copies it once.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
2
ms

Beats
90.74%
of users with Rust

Memory
2.16
MB

Beats
77.78%
of users with Rust