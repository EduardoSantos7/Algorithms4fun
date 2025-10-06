# Algorithm Idea

The first approach is not compliant since it's using extra memory, the idea is just to count the frecuency and then recreate the array from the beggining
The second approach is constant in memory but n^2 in time because everytime delete an element from the array happen the rest of the array have to be shifted
The third approach is constant spae and linear, in time it's using two pointer, the writter which is the slower pointer and the reader who checks that the current element is not the same as 2 before the writer.

# Complexity

Approach 1)

- Time: O(N)

- Space:O(N)

Approach 2)

- Time: O(N^2)

- Space:O(1)

Approach 3)

- Time: O(N)

- Space:O(1)


# Results

Approach 1)

Runtime
76
ms
Beats
91.40%

Memory
20.50
MB
Beats
46.06%

Approach 2)

Runtime
92
ms
Beats
21.43%

Memory
20.40
MB
Beats
46.06%

Approach 3)

Runtime
81
ms
Beats
75.75%

Memory
20.39
MB
Beats
79.26%