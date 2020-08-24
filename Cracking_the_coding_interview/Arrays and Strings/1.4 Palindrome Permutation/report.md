# Problem

Given a string, write a function to check if it's a permutation of a palindrome.

# Algorithm Idea

Count the frequency of the chars and verify that every char has an even count or just one char can has an odd length.

**Note:**

    - We should know that in order to have a palindrome is necessary to have the same count of letters.

    - We can split tthe problem in 2 question is this word a is the word a possible permutation and is a palindrome?

    - Quickly we realize that even palindromes are by definition permutation and in case of it would be odd len we can ignore the odd char so this ends in a simple question, is this a palindrome?

    - We should know that we can check for a palindrome using 2 pointers, just if the string couldn't be re arrenged if so we need to count the frequency of chars and at most 1 char can have odd length.

# Complexity

- Time: O(N) n is the length of the string.

- Space:O(c) c is the length of set of the unique chars
