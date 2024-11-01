# Algorithm Idea

The approach for counting hills and valleys in an integer list streamlines the process by iterating through the list just once, starting from the second element and ending at the second-to-last. It uses a single loop to both skip duplicates and count hills and valleys based on comparisons with the last unique value recorded. As the loop progresses, each number is compared to its previous significant neighbor and the next one; if it's distinctly higher or lower than both, it's counted as a hill or valley respectively. This method is efficient as it avoids additional storage and reduces the computational overhead by combining the deduplication and counting steps into one continuous operation, resulting in a time complexity of 
𝑂(𝑛), where 𝑛 is the number of elements in the list.

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Runtime
0
ms
Beats
100.00%

Memory
16.70
MB
Beats
18.69%