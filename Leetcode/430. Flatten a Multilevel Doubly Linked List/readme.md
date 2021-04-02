# Algorithm Idea

**Recursive Approach**

Each time you find an element with a child then save the rest of the list in a variable (last), put the child as next, and recurse the function passing as root the child node, also set child to None.

**Recursive Approach Optimization**

You will traverse each level twice due to each time you return you will move the pointer to the next element which is the level you just flatten. The approach is to keep the last element seen in the last level and when you get back inmediatly start from there.

**Iterative**

Create a stack to save the next element of each node with a child. Put the child as next and when you reach the end of the list check if the stack is empty if not push the element in the stack as the tail of the list and continue the iteration

# Complexity

**Recursive Approach**

- Time: O(N^2) Because where are re-iterating each level when we return 

- Space:O(D) where D is the Depth of the list

**Recursive Approach Optimization**

- Time: O(N) 

- Space:O(D) where D is the Depth of the list

**Iterative**

- Time: O(N) 

- Space:O(D) where D is the Depth of the list

# Results

**Recursive Approach**

**Python**

- Runtime: 48 ms, faster than 14.89% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.

- Memory Usage: 14.9 MB, less than 51.73% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.

**Recursive Approach Optimization**

**Python**

- Runtime: 36 ms, faster than 63.46% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.

- Memory Usage: 14.8 MB, less than 67.65% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.

**Iterative**

**Python**


- Runtime: 28 ms, faster than 95.55% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.

- Memory Usage: 14.8 MB, less than 67.65% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.