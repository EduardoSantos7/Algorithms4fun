# Algorithm Idea

Traverse the list with two pointers, where the second one moves till find a 0, meanwhile each non zero value is addem to a temporal counter. When it find a zero then the first pointers value become the counter, counter is restarted, second pointer becomes None or next if there is a next value and the first pointer next become the secn pointer while the first pointer moves to the current second. 

# Complexity

- Time: O(N)


- Space:O(1)

# Results

Runtime

128
ms
Beats
77.84%

Memory
60.33
MB
Beats
87.38%
