# Algorithm Idea

Iterate through the string, when you find an opening char ([, {, ( ) append it to a stack and when you find a closing char check whether it's the closing equivalent for the top element in the stack, if so then it's valid and continue else the string is invalid. If the string is valid then the stack should be empty at the end.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Rust)

- Runtime: 0 ms, faster than 100.00% of Rust online submissions for Valid Parentheses.

- Memory Usage: 2 MB, less than 77.66% of Rust online submissions for Valid Parentheses.
