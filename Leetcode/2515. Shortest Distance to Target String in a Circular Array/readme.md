# Algorithm Idea

Check if target exists: First, we check if the target exists in the words array. If it doesn't, we return -1.

Initialize variables: We get the length of the array n and initialize min_distance to a very large number (float('inf')) to ensure any valid distance will be smaller.

Calculate distances: We loop through the array to find all occurrences of the target. For each occurrence, we calculate the forward distance and the backward distance using modular arithmetic to handle the circular nature of the array. The forward distance is (i - startIndex) % n, and the backward distance is (startIndex - i) % n.

Update minimum distance: We update min_distance with the smaller of the current minimum distance, the forward distance, and the backward distance.

Return the result: Finally, we return the min_distance.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
60
ms
Beats
36.36%

Memory
16.46
MB
Beats
99.33%
