# Algorithm Idea

Approach 1)

Iterate the array until the previous to the last element
Compare every current element with the next, if it's the same then sum the same value to the current item (equivalent or multiply for two) and set the next to 0
Sort all the items moving the zeros at the end

Approach 2)

Iterate the array, for each element
Compare every current element with the next, if it's the same then sum the same value to the current item (equivalent or multiply for two) and set the next to 0
If current is different from 0 then add it to a new vector
After iterate all the items resize the array wih only the numbers different to zero to match the length of the first array and fill it with zeros

# Complexity

Approach 1)

- Time: O(n*log*n)

- Space:O(n)

Approach 2)

- Time: O(n)

- Space:O(n)

# Results

Approach 1)

Runtime
1 ms
Beats
88.24%
Memory
2.2 MB
Beats
5.88%

Approach 2)

Runtime
0 ms
Beats
100%
Memory
2.1 MB
Beats
23.53%
