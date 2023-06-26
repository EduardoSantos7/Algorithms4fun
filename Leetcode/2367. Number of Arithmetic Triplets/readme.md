# Algorithm Idea

Algorithm 1)

Convert the input list in a set and then traverse the set, for each number check if the number minus the diff and and the number minus tw times the diff are in the set, if so add 1 to a counter, return the counter at the end.

Algorithm 2)

Instead of build the seen array from the begining, build it on the fly by just iterate through the list of numbers and check in the seen set for num - diff and num - diff - diff, if both are present increase a counter. At the end of each iteration add the curren number to the seen set. At the end return the counter

# Complexity

Algorithm 1)

- Time: O(n)

- Space:O(n)

Algorithm 2)

- Time: O(1)

- Space:O(n)

# Results

Python)

    Algorithm 1)
    
    Runtime
    54 ms
    Beats
    76.97%
    Memory
    16.2 MB
    Beats
    97.2%
    
    Algorithm 2)
    
    Runtime
    45 ms
    Beats
    96.33%
    Memory
    16.2 MB
    Beats
    74.39%

Rust)

Algorithm 2)

Runtime
1 ms
Beats
75.86%
Memory
2.1 MB
Beats
24.14%

Golang)

Algorithm 2)

Runtime
0 ms
Beats
100%
Memory
2.4 MB
Beats
29.82%