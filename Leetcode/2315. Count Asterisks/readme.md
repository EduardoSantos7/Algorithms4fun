# Algorithm Idea

Create a boolean flag to determine if you are inside a pair of bar or no.
Create a counter to hold the result.
Iterate the letters in the string, for each letter check if:
    it's a bar (|), in this case set the flag to its opposite value
    if not bar but it's an asterik and the flag is in false, increment the counter by 1.
Return counter

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
33
ms
Beats
76.04%
of users with Python3\

Memory
16.54
MB
Beats
66.63%
of users with Python3