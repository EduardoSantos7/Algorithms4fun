# Algorithm Idea

Keep two counters for each side of the array, the first counter starts at 0 and the other counter starts at the sum of the array.
Iterate the list and recalculate right side by decreasing left side and current number and update the left counter by suming the current value

# Complexity

- Time: O(2N) -> O(n)

- Space:O(1)

# Results

Runtime
70 ms
Beats
88.14%

Memory
14.2 MB
Beats
55.5%
