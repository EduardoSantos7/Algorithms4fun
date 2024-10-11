# Algorithm Idea

Initialize a variable a equal to the integer division of high - low + 1 by 2. This will give us the number of even numbers between low and high (inclusive).
Return a + 1 if both low and high are odd numbers, else return a.
The reason why we add 1 in step 2 is that if both low and high are odd, then there is one more odd number (the middle number) than the even numbers.
The bitwise AND operator (&) is used to check if low and high are odd. If the least significant bit of low and high is 1, then it means they are both odd.
The final result of the function is the count of odd numbers between low and high (inclusive).

# Complexity

- Time: O(1)

- Space:O(1)

# Results

Runtime
33
ms
Beats
66.54%

Memory
16.60
MB
Beats
7.42%
