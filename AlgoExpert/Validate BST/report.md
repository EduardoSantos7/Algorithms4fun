# Algorithm Idea

Every node in the BST has a maximum possible value and a minimum possible value. In other words, the value of any given node in the BST must be strictly smaller than some value (the value of its closest right parent) and must be greater than or equal to some other value (the value of its closest left parent). Validate the BST by recursively calling the validateBst function on every node, passing in the correct maximum and minimum possible values to each. Initialize those values to be -Infinity and +Infinity.

# Complexity

- Time: O(N)

- Space:O(d)

# Results
