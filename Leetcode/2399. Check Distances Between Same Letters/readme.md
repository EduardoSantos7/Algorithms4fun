# Algorithm Idea

Create set to store the letters seen.
Iterate the letters of the string, if the letter is already seen continue if not:
Gets its distance from distances array, use the substraction of ascii values (current char - 97 (a)) to index that array
create a variable other_char where is value is the sum of current index plus the distance aplus 1.
Verify the length of the string is bigger than other_char and the strinf index in other_char index is the same as current index, in that case save the current char in the set and continue in any other case return False.
If the loop was completed return true

# Complexity

- Time: O(n) where n is the length of the string

- Space:O(n)

# Results

Runtime
45
ms
Beats
54.33%
of users with Python3
Memory
16.58
MB
Beats
50.87%
of users with Python3
