# Algorithm Idea

Using BFS create a work queue to keep track of the current level, at the same time keep a counter for the current sum of values for the level. While traversing tree instead of append the next child to the queue add it to this "work queue", the idea is that the original queue only have the elements of this level, when the queue is empty that means that you have traverse all the level if the work queue is empty that means that was the last level return the current sum if not set the queue to the work queue, reset the work queue and reset the current sum.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
225 ms
Beats
42.54%
Memory
20.7 MB
Beats
42.7%