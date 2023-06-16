# Algorithm Idea

Approach 1) Sort the list of number and then iterate the unsorted array and find the index in the sorted array, map the rank and push it to an answer list that you will return
Approach 2) Use a MaxHeap to push the items in the array, then push out them and map the rank, push the rank in a list you will return

# Complexity

- Time: O(nLogn)

- Space:O(n)

# Results

Approach 1)

Runtime
422 ms
Beats
13.70%
Memory
16.6 MB
Beats
82.15%

Approach 2)

Runtime
93 ms
Beats
37.61%
Memory
17.7 MB
Beats
13.7%