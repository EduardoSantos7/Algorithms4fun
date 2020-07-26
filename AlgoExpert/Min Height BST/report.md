# Algorithm Idea

Grab the middle element of the array, and make that element be the root node of the BST. Then, grab the middle element between the beginning of the array and the first middle element, and make that element be the root of the BST's left subtree; similarly, make the middle element between the end of the array and the first middle element be the root of the BST's right subtree. Continue this approach until you run out of elements in the array.

# Complexity

- Time: O(N)

- Space:O(N)

# Results
