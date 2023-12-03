# Algorithm Idea

Initialize an Array: Create an array result of length num_people, initially filled with zeros. This array will store the final distribution of candies to each person.

Distribute Candies: Start with a variable candy set to 1, which represents the number of candies to give to the current person. Iterate over the people in a loop, and for each person:

- Check if the remaining candies are sufficient to give the current amount (candy). If not, give them all the remaining candies.
- Update the result array by adding the number of candies given to the current person.
- Decrease the total number of candies by the number of candies given.
- If the candies are finished, break out of the loop.
- Increment the candy variable for the next person.

Handle Wrap Around: The above steps will need to handle the case when you reach the last person in the row. In that case, start again from the first person.

Return Result: Once all candies are distributed, return the result array.

# Complexity

- Time: O(n) where n is the number of candies

- Space:O(m) where m is the number of people

# Results

Runtime
35
ms
Beats
94.44%
of users with Python3
Memory
16.50
MB
Beats
9.42%
of users with Python3