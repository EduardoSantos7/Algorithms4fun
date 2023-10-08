# Algorithm Idea

start is initialized to 0 as the starting index.
_sum is calculated as the sum of the elements from index start to index k-1 in nums.
max_avg is set to the initial average by dividing _sum by k.
n is set to the length of nums.
A loop iterates from index k to n-1.
In each iteration, _sum is updated by adding the element at index i and subtracting the element at index start. This effectively moves the sliding window.
start is incremented by 1 to move the window.
avg is calculated as the new average by dividing _sum by k.
If avg is greater than the current max_avg, max_avg is updated to the new value.
After the loop ends, the final maximum average is returned as the result.


# Complexity

- Time: O(n)

- Space:O(1)

# Results

pYTHON)

Runtime
1147 ms
Beats
91.55%
Memory
27.9 MB
Beats
99.47%

C#)

Runtime
311 ms
Beats
15.29%
Memory
59.9 MB
Beats
41.91%

Golang)

Runtime
172 ms
Beats
80.12%
Memory
7.6 MB
Beats
99.1%

Rust)

Runtime
23 ms
Beats
78.29%
Memory
2.9 MB
Beats
63.82%