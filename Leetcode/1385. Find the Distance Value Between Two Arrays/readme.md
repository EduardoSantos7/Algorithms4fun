# Algorithm Idea

Approach 1)

This solution uses a bucketing strategy. Each value from arr2 is assigned a bucket based on the value divided by d. Only the minimum and maximum values of each bucket are stored. This is because any value x from arr1 must check only the nearest neighbors in the corresponding buckets to ensure there is no arr2[j] such that |x - arr2[j]| < d. By checking the current bucket and immediate neighboring buckets (to handle edge cases), we efficiently determine if x meets the distance criteria.

Approach 2)

This solution employs binary search using Python's bisect module. First, array b (arr2) is sorted. For each element x in a (arr1), the limits x-d and x+d are determined. The bisect_left function finds the insertion points for these limits in b. If these points indicate that no element in b is within the distance d of x, then x contributes to the distance value. The specific checks ensure that no elements of b lie between x-d and x+d.

# Complexity

Approach 1)

Time: O(N + M) where N is the length of arr1 and M is the length of arr2. This includes the time to initialize buckets and then check each element in arr1 against the relevant buckets.
Space: O(U) where U is the number of unique keys or buckets. In the worst case, this can be large depending on the range and distribution of arr2, but it is typically less than M.

Approach 2)

Time: O(M log M + N log M) where M is the length of b (arr2) and N is the length of a (arr1). Sorting b takes O(M log M), and each search operation takes O(log M), applied N times.
Space: O(1) not considering the space for sorting b. If additional space for sorting is considered, it becomes O(M) for a sorted copy of b.

# Results

Approach 1)

Runtime
55
ms

Beats
98.99%
of users with Python3

Memory
16.69
MB

Beats
74.75%
of users with Python3

Approach 2)

Runtime
65
ms

Beats
92.09%
of users with Python3

Memory
16.78
MB
Beats
28.79%
of users with Python3

Runtime
0
ms

Beats
100.00%
of users with Rust

Memory
1.96
MB

Beats
100.00%
of users with Rust