# Algorithm Idea

Create a dictionary where the keys are the sorted set of letters in the string and the values are the count of occurrences
For each set calculate the number of pairs by calling a DP method which will do the next:
if length is equals 1 return o, equals 2 return 1 and everything else return the sum between this DP function call passing param as input - 1 plus length -1. You can optimize this using a dictionary to remember the numbers already computed.
Sum up this pairs count in to a total counter.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
52
ms
Beats
95.48%
of users with Python3
Memory
16.86
MB
Beats
10.15%
of users with Python3