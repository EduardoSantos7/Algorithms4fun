# Algorithm Idea

The first approach is to use recursion. The second one is an improvement over the first approach which uses an array tto store previous calculations. And the last approach is to iterate and update the values.


# Complexity

- Time:

    - Recursive
        - O(2^N) - On each iteration we're creating 2 new instances in the stack
    
    - Recursive Improved
        - O(N) - We only calculate the fib number once per each number
    
    - Iterative
        - O(N)

- Space:

    - Recursive
        - O(N) - We only store N calls iin the stack
    
    - Recursive Improved
        - O(N) - The numbers in the dict
    
    - Iterative
        - O(1)

# Results

