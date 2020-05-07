# Algorithm Idea
Traverse the string; When the current character is `(` then add this value and its index to the stack. When the character is `)` and if the stack is not empty then pop the element from the stack and add its value into the corresponding positiion in the array, also adds the `)` in the current position. In case the stack is empty just skip it, if the char is other char add it in the current position. Finallly just join the result array.

NOTE: Using join is more convinient because we only perform one action, iin other cases we would be rebuilding the string with each change every time.


# Complexity

- Time: O(N)
- Space:O(N)

# Results

Python)

    - Runtime: 88 ms, faster than 96.58% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
    
    - Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.