# Algorithm Idea

Create a hashset with the broken keys
Iterate the string checking if the current char is inside the set, in that case set a flag to true.
When you find a " " (space) check if that flag is true, in that case set it to false and continue. If it's false then just increment a counter.
After iterate all the characters return the counter if the flag is true else return the counter + 1.

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Runtime
47
ms
Beats
64.86%

Memory
38.52
MB
Beats
83.78%
