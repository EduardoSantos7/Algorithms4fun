# Algorithm Idea

Iterate the domains in the input, per each entry split it by the space character, the first string should be cast to int since it is always a number. The second string, split it by "." and per every subdomain check if the count exists to set it or update it. Return a list base on the dictionary that keep the count of visit per subdomain.


# Complexity

- Time: O(n) where n is the number of domains in the list, other way to see it is n*c where c are the average number of characters per domain

- Space:O(n)

# Results

Runtime
53
ms

Beats
60.36%
of users with Python3

Memory
16.46
MB

Beats
98.18%
of users with Python3