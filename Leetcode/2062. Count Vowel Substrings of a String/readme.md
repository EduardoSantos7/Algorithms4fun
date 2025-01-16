# Algorithm Idea

Approach 1)

Brute force, for each character that is a vowel, perform another iteration to check till where the vowels continue, add each new to a set, for every time that you find one vowel and that set has 5 vowels increment the counter by one.

Approach 2)

Iterate the array and for each consonant update a variable to keep track the last index of a consonant.
For a vowel update the last index seen of that vowel, and increase the counter by the maximum number in between 0 and the difference between the minimum index of the consonants where -1 represents that we haven't seen it, and last consonant index.

# Complexity

Approach 1)

- Time: O(N^2)

- Space:O(1)

Approach 2)

- Time: O(N)

- Space:O(1)

# Results

Approach 1)

Runtime
47
ms
Beats
70.03%

Memory
16.54
MB
Beats
38.55%

Approach 2)

Runtime
36
ms
Beats
88.70%

Memory
16.60
MB
Beats
38.55%