# Algorithm Idea

Create a dictionary to count the frequency of elements.
Create a set to keep the left side unique elements, and an array of the same length as the input array.
iterate the input array and for each number:
add it to the set
decrease the frequency from the hasmap
if the frequeency is zero then delete the key from the map
insert in the position i the difference between the length of the set and the length of keys in the map
return the array

# Complexity

- Time: O(n)

- Space:O(n)

# Results

Runtime
84
ms

Beats
88.07%
of users with Python3

Memory
16.50
MB

Beats
73.78%
of users with Python3