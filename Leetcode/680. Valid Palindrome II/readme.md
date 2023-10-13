# Algorithm Idea

Iterate the string with two pointers, one from the beginning and the other one from the end.
If the characters in those positions are the same. Increase the point of the start, and decrease the pointer from the end.
If it's different  try to check if the moving one of the pointers at the time would produce a palindrome

# Complexity

- Time: O(n)

- Space:O(1) // In rust we can say this is n because we have to convert it to an array of char but in other languages this might be seen as constant

# Results

Runtime
5 ms
Beats
29.41%
Memory
2.4 MB
Beats
26.47%