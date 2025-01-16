# Algorithm Idea

Approach 1)

Iterate from 1 to 1000 inclusive checking how many numbers are not there and then if the number of missing number is same as K then return the current number missing. If after 1000 you haven't return then return the a 1000 + k - the missing number

Approach 2)

Binary Search

# Complexity

Approach 1)

- Time: O(N)

- Space:O(N)

Approach 2)

- Time: O(LogN)

- Space:O(1)

# Results

Approach 1)

Runtime
45
ms
Beats
86.64%

Memory
16.65
MB
Beats
66.83%

Approach 2)

Runtime
48
ms
Beats
74.78%

Memory
16.76
MB
Beats
27.41%