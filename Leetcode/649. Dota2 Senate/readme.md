# Algorithm Idea

Use a Q to track the senators with right for vote. Keep 4 counters, 2 for cou t the available senator of each party and the other two to count the senators that will be banned from the other party. While both parties has a senator then iterate the string and if the current char is not banned then increment the cou ter of senators to ban in the other party and requeue this senator else decrease the baned counter and not append. Return theparty with a valid senator

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
33 ms
Beats
75%
Memory
2.2 MB
Beats
87.50%

