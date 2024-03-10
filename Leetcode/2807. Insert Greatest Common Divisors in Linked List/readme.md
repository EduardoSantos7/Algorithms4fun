# Algorithm Idea

Use two pointers to iterate the linked list, one from the head and the second one from the next element.
While the pointer in the front is different from null:
- calculate the gcd in between the values of the two pointers
- create a new node with tha value
- make the pointer in the back to point its next reference to the new node
- and the next reference of the new node to the pointer in the front
- make the pointer in the back to point to the one in the front and the one in the front to its next value

# Complexity

- Time: O(n) because we have to iterate all the list

- Space:O(n) because you will have to insert n-1 elements

# Results

Runtime
59
ms
Beats
93.92%
of users with Python3

Memory
19.61
MB
Beats
46.70%
of users with Python3