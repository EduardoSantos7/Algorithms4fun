# Algorithm Idea

Traverse all the levels and store each level in a result list, each current level are the values of all nodes in the queue, next level is the list all the children in the current level, as we are traversing by level the quue is update with the next level in this way each next level becomes the current level in the next iteration.


# Complexity

- Time: O(N)

- Space:O(N)

# Results

Python)

    - Runtime: 40 ms, faster than 99.31% of Python3 online submissions for N-ary Tree Level Order Traversal.

    - Memory Usage: 15.6 MB, less than 100.00% of Python3 online submissions for N-ary Tree Level Order Traversal.

Go)

    - Runtime: 0 ms, faster than 100.00% of Go online submissions for N-ary Tree Level Order Traversal.

    - Memory Usage: 4.3 MB, less than 100.00% of Go online submissions for N-ary Tree Level Order Traversal.