# Algorithm Idea

Approach 1)

For each index (aassume the index is that center) calculate odd and even palindromes.


Approach 2)

Manacher algorithm: https://cp-algorithms.com/string/manacher.html

Similarly to the previous approach we expand from the center but instead of recalculate the palindrome every time is just do it when it's out of the boundary, else reuse the previous one and uses simetry to avoid recompute.

# Complexity

Approach 1)

- Time: O(N)

- Space:O()

Approach 2)

- Time: O(N)

- Space:O(N)

# Results

Approach 1)

Runtime

128
ms
Beats
63.07%

Memory
17.57
MB
Beats
97.82%

Approach 2)

Runtime

3
ms
Beats
99.73%

Memory
17.94
MB
Beats
34.08%