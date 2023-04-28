# Algorithm Idea

Due to the graph is not necessary fully conected we should check each possibe root. We have many posible roots due to the graph is not rooted. We will use the colorized idea, using BFFS we will traverse the graph from each root and each vertice will get a color and its neighbors will get the other color. We should check that our neighbors doesn't have the same color that the vertice

# Complexity

- Time: O(N*(V*E)) -> Worst Case is O(N^2) ; Best Case is O(N)

- Space:O(N)

# Results

Python)

    - Runtime: 180 ms, faster than 91.43% of Python3 online submissions for Is Graph Bipartite?.

    - Memory Usage: 14.2 MB, less than 48.22% of Python3 online submissions for Is Graph Bipartite?.

Rust)

    - Runtime: 4 ms, faster than 78.26% of Rust online submissions for Is Graph Bipartite?.

    - Memory Usage: 2.1 MB, less than 65.22% of Rust online submissions for Is Graph Bipartite?.
