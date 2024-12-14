# Algorithm Idea

Approach 1)

Create dictionary to store the elements seen.
Iterate the array and check which elements is bigger in the current pair.
Generate a new pair where the smaller number is always in the beginning (or the other way around, the idea is to ensure that (x, y) would be stored in the same place as (y, x))
Count the frequencies of this new pairs.
Iterate this frequencies, and for all of them that are bigger than 0 get the total number of pairs which is n*(n-1)/2.
Return the sum all the total number of pairs.

Approach 2)



# Complexity

Approach 1)

- Time: O(n)

- Space:O(n)

Approach 2)



# Results

Runtime
176
ms
Beats
100.00%
of users with Python3
Memory
26.01
MB
Beats
78.90%
of users with Python3

Runtime
3
ms
Beats
100.00%
of users with Rust
Memory
4.35
MB
Beats
20.00%
of users with Rust