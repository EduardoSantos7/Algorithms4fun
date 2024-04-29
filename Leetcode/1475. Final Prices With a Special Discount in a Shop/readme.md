# Algorithm Idea

Brute force approach is to iterate all thje numbers and in each iteration, iterate the numbers after the current one to find the appropriate discount.

`Monotonic Stack Technique`

A stack is used to keep track of indices of list elements in a "monotonic" order — either strictly increasing or strictly decreasing values depending on the problem requirement. In this particular problem, the stack is used to hold indices of the prices list in a way that the prices corresponding to these indices are maintained in a non-increasing order. Here’s how it works:

Traverse through each price: You go through each element in the prices list.
Process Stack: As long as the stack is not empty and the current price is less than or equal to the price at the index stored at the top of the stack:
Pop the stack, which means you're considering that top index for discount calculation.
Update the result for that index by subtracting the current price (acting as a discount).
Store Current Price: Append the current price to the result list — this represents the price without any discount (initially).
Push Current Index: Push the current index onto the stack to keep track of it for possible future discounts.

# Complexity

Brute force)

- Time: O(n^2)

- Space:O(1)
  
Monotonic Stack)

- Time: O(n)

- Space:O(n) in the worst case for the stack if all elements are processed without finding a smaller subsequent price (i.e., prices are in decreasing order).

# Results

Brute force)

Runtime
56
ms
Beats
16.27%
of users with Python3

Memory
16.66
MB
Beats
66.21%
of users with Python3

Monotonic Stack)

Runtime
49
ms
Beats
58.08%
of users with Python3

Memory
16.72
MB
Beats
19.40%
of users with Python3