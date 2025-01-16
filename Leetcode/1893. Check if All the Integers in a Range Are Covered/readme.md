# Algorithm Idea

There're multiple ways to resolve this problem but the main steps are

1) Get the elements in the ranges into a structure that allows o(1) checks
2) Iterate the range from left to right to check if this element is present

The tricky part is the first point, we can achieve it using an array to mark the starts and end and then compute the sum in those ranges, or using a set to store all the elements, but this last approach will required O(n) memory

# Complexity

- Time: O(N + R) - where N is the range between left and right in the params and R is the number of ranges

- Space:O(1)

# Results

Runtime
0
ms
Beats
100.00%

Memory
16.66
MB
Beats
25.04%