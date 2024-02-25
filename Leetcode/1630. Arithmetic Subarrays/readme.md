# Algorithm Idea

We can implement check more efficiently! While it is true that any arithmetic sequence is sorted, we don't need to exploit this fact to determine if arr is an arithmetic sequence.

Let's say arr has a length of n, and we have the maximum element in arr as max and the minimum element as min.

If arr were to form an arithmetic sequence, then the difference diff that defines the sequence must be equal to (max−min)/n−1
Why? Because min must be the first element of the sequence and max must be the final element of the sequence. Thus, if we started at min and iterated to max, we would require n−1n - 1n−1 iterations. On each iteration, our value would increase by diff (by definition).

By starting at min and ending at max, we do increments of diff every step, we cover a total distance of max - min. to see if all the numbers are contained in the set.

# Complexity

- Time: O(m*n) where m are the queries, in the worst case each query will be n

- Space:O(n)

# Results

Runtime
253
ms
Beats
7.28%
of users with Python3

Memory
16.97
MB
Beats
49.95%
of users with Python3