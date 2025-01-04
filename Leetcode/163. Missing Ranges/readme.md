# Algorithm Idea

One of the key insights is that the input is a sorted array. Since the range lower and upper could be too big to iterate and provoke time limit errors, we can use this property to reduce the time.

We can compute in a constant time the range missing before and after the first and last digit of the input array. Since the numbers missing inside the array might be too large a way to do it is using two pointers.

One pointer points to the first element in the list and the second one to the second. This pointers will move 1 by 1. Use another two pointers to check the start and end of the possible missing range. We have a missing range if the start which is the value of the pointer to number 1 + 1 is different from the value pointed by pointer 2. In this case we append a list containing this range.

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Runtime
0
ms
Beats
100.00%

Memory
18.02
MB
Beats
5.28%