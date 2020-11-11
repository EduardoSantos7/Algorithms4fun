# Algorithm Idea

Iterate the string and save the index of chars you haven't see before and if you have see it then compute the current substring and if it is bigger than the previous one then update the max len. Also keep a flag to ensure that you have at least 1 char repeated if not then return -1

# Complexity

- Time: O(N)

- Space:O(N)

# Results

Python)

- Runtime: 28 ms, faster than 88.58% of Python3 online submissions for Largest Substring Between Two Equal Characters.

- Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Largest Substring Between Two Equal Characters.

Rust)

- Runtime: 0 ms, faster than 100.00% of Rust online submissions for Largest Substring Between Two Equal Characters.

- Memory Usage: 2 MB, less than 100.00% of Rust online submissions for Largest Substring Between Two Equal Characters.

Golang)

- Runtime: 0 ms, faster than 100.00% of Go online submissions for Largest Substring Between Two Equal Characters.

- Memory Usage: 2 MB, less than 100.00% of Go online submissions for Largest Substring Between Two Equal Characters.