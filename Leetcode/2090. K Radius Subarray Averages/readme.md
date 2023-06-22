# Algorithm Idea

Init an array of length of the input array with all elements in -1. Calculate the sum of the first 2*k+1 elements.From iterate nums k to length of nums - k. Update the answer created at position i with the average which is the sum precalculated divided by 2*k+1 and just take the integer part. Update the count by decreasing it by the number in i-k and suming the number in i+k+1, check for index index error before sum. Return array. 

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
1581 ms
Beats
92.66%
Memory
35 MB
Beats
41.70%