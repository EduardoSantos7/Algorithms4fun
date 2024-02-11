# Algorithm Idea

The idea is to iterate the list of logs to construct a dictionary where the user Id will be the key and the value will be a set for the minutes in which actions took place. After construct this, iterate the map and get the count of actions per user id, then in the response array increase the counter by one in the position of this count minus one since the array is 1-index.

# Complexity

- Time: O(N) where N is the number of logs

- Space:O(N) caused by the dictionary space

# Results

Runtime
699
ms
Beats
85.48%
of users with Python3

Memory
27.22
MB
Beats
63.08%
of users with Python3