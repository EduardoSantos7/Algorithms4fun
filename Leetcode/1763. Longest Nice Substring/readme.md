# Algorithm Idea

First generates a set of all characters present between two indices (left and right). Then, it iterates over each character in this substring range. If it finds a character for which either the lowercase or uppercase variant is not in the character set, it splits the problem into two subproblems: one for the substring before this character (prefix) and one for the substring after this character (suffix). It recursively solves for both subproblems and compares their results. The algorithm returns the longer of the two "nice" substrings. If no such character (that violates the "nice" condition) is found, it means the entire substring from left to right is "nice," and it returns this substring's indices. This approach effectively uses divide and conquer to break down the problem into smaller, manageable parts, evaluating each character and its compliance with the "nice" criteria, thereby recursively determining the longest "nice" substring.

# Complexity

- Time: O(N^2)

- Space:O(N)

# Results

Runtime
3
ms
Beats
92.04%

Memory
13.88
MB
Beats
72.90%

