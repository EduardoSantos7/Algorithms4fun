# Problem

Implement a method to perfom a basic string compression using the count of repeating chars. If the `compressed` won't be smaller than the input then return the input.

# Algorithm Idea

We can check at the begging if the length would be smaller instead of build a string that probably we won't use. If it's we can use this data to set the array capacity (In python that's no too helpful). We'll iterate the string keeping the count and when we found a different char just append to the array at the end just join the array.

# Complexity

- Time: O(N)

- Space:O(C) C is the size of the compressed string.
