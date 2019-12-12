# Algorithm 1 Idea
Use BFS, a parent node will link ts left child with the right one, and the parent will save its children with a reference to himself in the queue. If a node has a parent but not a next that means that his father didn't link him, so it will link himself using his parent as reference.

# Algorithm 1 Complexity
Time: O(n) - All the nodes are traversed.
Space:O(n) - Queue used to perform the BFS.

# Algorithm 2 Idea
It's a level traverse too, but in this case, we don't need a queue or pass the parent reference because the parent will link the right child too if he has the next element.

# Algorithm 2 Complexity
Time: O(n) - All the nodes are traversed.
Space:O(1) - Only 2 variables are needed.

# Algorithm 1 Results
Runtime: 64 ms, faster than 75.80% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.

# Algorithms 2 Results
Runtime: 56 ms, faster than 95.88% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.

# Differences
The second one is smaller, slightly faster and uses less memory.