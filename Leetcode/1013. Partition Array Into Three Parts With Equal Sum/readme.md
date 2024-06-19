# Algorithm Idea

Approach 1)

Loop through the array A, and compute part of sum; if the average value is found, reset the part to 0, and increase the counter.

By the end if the average can be seen for at least 3 times and if the total sum is divisible by 3;, return true; otherwise return false.

if the average (sum / 3) found 2 times before the end of the array, then the remaining part is also equals to the average. Therefore, no need to continue after the counter reaches 3.

Approach 2)

Staring from the two ends of the input array, accumulate left and right parts till getting the average values.


If having found average values on both parts before the two pointers meet, return true; otherwise, return false.


# Complexity

Approach 1)

- Time: O(n)

- Space:O(1)

Approach 2)

- Time: O(n)

- Space:O(1)

# Results

Approach 1)

Runtime
241
ms
Beats
37.42%

Memory
22.97
MB
Beats
98.83%

Approach 2)

Runtime
271
ms
Beats
5.08%

Memory
23.08
MB
Beats
92.05%