# Algorithm Idea

Create two variables to track the max length and a counter which represent the numbers of time you have seen the biggest element.
Iterate the array, each item will be an array of two elements, pick the smaller one.
Compare the number you picked with the current biggest number you have it's bigger then reset your counter and set
your biggest tracker variable to this new value.
Return the count

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Runtime
158
ms
Beats
75.57%

Memory
17.20
MB
Beats
51.63%
