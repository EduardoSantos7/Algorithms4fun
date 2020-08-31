# Algorithm Idea

The problem wants us to reform the linked list structure, such that the elements lesser that a certain value x, come before the elements greater or equal to x. This essentially means in this reformed list, there would be a point in the linked list before which all the elements would be smaller than x and after which all the elements would be greater or equal to x. Let's call this point as the JOINT.


Reverse engineering the question tells us that if we break the reformed list at the JOINT, we will get two smaller linked lists, one with lesser elements and the other with elements greater or equal to x. In the solution, our main aim is to create these two linked lists and join them.

We can take two pointers before and after to keep track of the two linked lists as described above. These two pointers could be used two create two separate lists and then these lists could be combined to form the desired reformed list.

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Python)

- Runtime: 40 ms, faster than 55.41% of Python3 online submissions for Partition List.

- Memory Usage: 14.1 MB, less than 5.30% of Python3 online submissions for Partition List.