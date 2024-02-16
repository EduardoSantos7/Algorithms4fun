# Algorithm Idea

Iterate the list of numbers while counting their frequency in a hashmap of even numbers. After update the frequency check if it's bigger that a counter initializated in the minimus number possible, this way we save an iteration to check the bigger number. Then iterate the keys and values in the map, if the value is the same as current maximum counter then store the numbe rin a list. Return the first element if the list only conain 1 element, if contains more return the min of the list else return -1

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
215
ms
Beats
80.68%
of users with Python3
Memory
17.27
MB
Beats
47.17%
of users with Python3