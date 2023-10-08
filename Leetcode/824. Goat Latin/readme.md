# Algorithm Idea

Split the sentence by space to get a list of words. For each word check the first char. Execute this rules:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

After create the new word append it in a list, after process all the words return the array of new words as string concatenating every word by an space.

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
47 ms
Beats
61.53%
Memory
16.2 MB
Beats
68.61%