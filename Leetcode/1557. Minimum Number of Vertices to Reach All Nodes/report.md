# Algorithm Idea

Approach 1) Use an array to count income edges and after count check which ones has zero and return them

Approach 2) Set substraction, as we only care about 2 sets: the firsst one is the numbers from 0 to n-1 and the second one the edges with zero incoming arrows we can just substract them.

# Complexity

Approach 1)

- Time: O(N)

- Space:O(N)

Approach 2)

- Time: O(N)

- Space:O(1)

# Results

Approach 1) 

- Python

    - Runtime: 1600 ms, faster than 60.11% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.

    - Memory Usage: 52.7 MB, less than 21.09% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.

Approach 2)

- Python)

    - Runtime: 1460 ms, faster than 66.32% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.

    - Memory Usage: 52.7 MB, less than 20.12% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
