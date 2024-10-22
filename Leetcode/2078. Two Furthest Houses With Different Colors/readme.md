# Algorithm Idea

I first though that this will be O(N^2) but quicly think that maybe I can use a sliding window approach, because you know once you find that the next one is different then the current max is 1 and from there it can only grow, but then I noticed, the biggest difference is always from the start/end to the further different color. Then I just need two pointers to keep moving in each direction and return the biggest difference.

Init to pointers, one from 0 and the other one from the last element, and a variable answer.
In a for loop of N - 1 iterations (where N is the length of the array)
Move each cursor in its respective direction.
Compare if the current number of each pointer is different from the first and last color respectively. If it's different update the answer variable with the current value of start/(n - end - 1).
Return the variable answer

My post in leetcode: https://leetcode.com/problems/two-furthest-houses-with-different-colors/solutions/5952921/fastest-solution-in-one-pass/

# Complexity

- Time: O(N)

- Space:O(1)

# Results

Runtime
0
ms
Beats
100.00%

Memory
16.79
MB
Beats
7.89%