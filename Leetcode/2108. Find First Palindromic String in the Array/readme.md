# Algorithm Idea

Approach 1)

For each word reverse it and check if it's the same to the original

Approach 2)

Use two pointer to check if the characters are the same in reverse order for each word

return the first that match the condition for both approaches

# Complexity

Approach 1)

- Time: O(n*m) where n is the number of words and m is the average length of a word

- Space:O(n) because we create n new strings

Approach 2)

- Time: O(n*m)

- Space:O(1)

# Results

Approach 1)

Runtime
150
ms
Beats
5.27%
of users with Python3
Memory
16.87
MB
Beats
5.72%
of users with Python3

Approach 2)

Runtime
79
ms
Beats
52.60%
of users with Python3
Memory
16.66
MB
Beats
70.81%
of users with Python3