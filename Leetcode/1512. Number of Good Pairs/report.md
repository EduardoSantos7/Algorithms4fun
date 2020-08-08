# Algorithm Idea

Traverse the array and count the frequency of each element. If the current number was seen before then the repetions are counted as good pairs and increased by one.

Other approach will be to use 2 for loops and avoid the hashmap that will be O(1) in memory but O(N^2) in runtime.

# Complexity

- Time: O(N)

- Space:O(N)

# Results

Python)

    - Runtime: 28 ms, faster than 95.49% of Python3 online submissions for Number of Good Pairs.

    - Memory Usage: 13.9 MB, less than 35.97% of Python3 online submissions for Number of Good Pairs.

Rust)

    - Runtime: 0 ms, faster than 100.00% of Rust online submissions for Number of Good Pairs.

    - Memory Usage: 2 MB, less than 65.08% of Rust online submissions for Number of Good Pairs.
