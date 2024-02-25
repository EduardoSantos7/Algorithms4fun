# Algorithm Idea

The algorithm finds the length of the longest consecutive sequence in an unsorted array by first converting the array into a set for O(1) lookup times and eliminating duplicates. It iterates through each unique number, extending the search in both forward and backward directions to find consecutive sequences, while a secondary set tracks numbers already considered in any sequence to avoid redundancy. The length of each found sequence is compared to maintain the maximum length found so far. By checking each number at most twice (once in each direction) and using sets for fast lookups and to avoid reprocessing elements, the algorithm achieves O(n) time complexity, where n is the number of elements in the array, making it efficient and scalable.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
355
ms
Beats
66.50%
of users with Python3

Memory
36.62
MB
Beats
8.57%
of users with Python3