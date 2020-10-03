# Algorithm Idea

Approach 1)

If the values of p and q are bigger than the root then call again the function passing the right node as root, if booth are smaller then pass the left, if neither of the prrevious conditions are true then you are in the LAC node.

# Complexity

Approach 1)

- Time: O(d) - Deep, in case is balanced if not then it's N

- Space:O(d) - Deep, in case is balanced if not then it's N

Approach 2)

- Time: O(N)

- Space:O(1)

# Results

Aproach 1)

Python)

- Runtime: 72 ms, faster than 97.19% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

- Memory Usage: 18 MB, less than 14.42% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

Approach 2)

Python)

- Runtime: 64 ms, faster than 99.90% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

- Memory Usage: 18.1 MB, less than 5.30% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.