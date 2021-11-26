# Algorithm Idea

Core Idea: A palindrome is conform by pairs of chars and at max 1 single char which is in the middle.

Approach 1)

Use a dictionary to count the char frequency. Then for each char get the count an use a counter to add the integer part which is divisible by 2 (ex. when 7 you will add 6). The module is added in another counter. By the end return the counter of pairs plus one if there is one or more solo chars.

This is the same idea of approach 1 (2 loops) but with an optimization (1 loop):

Approach 2)

Use a set to store solo chars, iterate over them chars in s if the char is in the solo set then increase a pairs counter and remove the char from solo set. If the char is not in the set then add it. Return the count of pairs multiplied by 2 and add 1 if the set of solo chars is not empty.

# Complexity

- Time: O(n)

- Space:O(1): the space for our count, as the alphabet size of s is fixed. We should also consider that in a bit complexity model, technically we need O(logN) bits to store the count values.

# Results

Python)

Approach 1)

- Runtime: 32 ms, faster than 76.70% of Python3 online submissions for Longest Palindrome.

- Memory Usage: 14.3 MB, less than 26.45% of Python3 online submissions for Longest Palindrome.

Approach 2)

- Runtime: 39 ms, faster than 28.92% of Python3 online submissions for Longest Palindrome.

- Memory Usage: 14.3 MB, less than 57.32% of Python3 online submissions for Longest Palindrome.

Rust)

Approach 1)

- Runtime: 0 ms, faster than 100.00% of Rust online submissions for Longest Palindrome.

- Memory Usage: 2 MB, less than 67.86% of Rust online submissions for Longest Palindrome.

Approach 2)

- Runtime: 0 ms, faster than 100.00% of Rust online submissions for Longest Palindrome.

- Memory Usage: 2.2 MB, less than 32.14% of Rust online submissions for Longest Palindrome.
