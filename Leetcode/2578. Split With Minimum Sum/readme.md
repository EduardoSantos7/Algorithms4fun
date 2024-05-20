# Algorithm Idea

Approach 1)

The idea is based on split the digits into two new numbers in a way tht each current bigger digit is in each number starting from the lowe unit. For example if the number is 1234 the digits are 1,2,3,4. Then 4 will go as the lower unit in num 1 and 3 in num 2 then 2 and 1 respectively in the next unit forming 42 and 31. To get the digits in the right order sort is needed, 

Approach 2)

Similar idea but instead of sort them just count their frequency with a dictionary and then iterate from 1 to 10 looking in the dictionary for that number and assign each occurrence to one of the resulting numbers. This avoid sorting. 

# Complexity

Approach 1)

- Time: O(nlogn)

- Space:O(n)

Approach 2)

- Time: O(n)

- Space:O(n)

# Results

Approach 1)

Runtime
30
ms
Beats
83.97%
of users with Python3

Memory
16.50
MB
Beats
89.89%
of users with Python3

Approach 2)

Runtime
37
ms
Beats
45.42%
of users with Python3

Memory
16.64
MB
Beats
12.98%
of users with Python3