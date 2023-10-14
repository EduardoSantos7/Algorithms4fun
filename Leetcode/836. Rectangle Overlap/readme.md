# Algorithm Idea

The answer for whether they don't overlap is LEFT OR RIGHT OR UP OR DOWN, where OR is the logical OR, and LEFT is a boolean that represents whether rec1 is to the left of rec2. The answer for whether they do overlap is the negation of this.

The condition "rec1 is to the left of rec2" is rec1[2] <= rec2[0], that is the right-most x-coordinate of rec1 is left of the left-most x-coordinate of rec2. The other cases are similar.

Note: we should also check if either of the rectangle is actually a line.
If this is the case, then we cannot have any positive overlapping according to the definition.

# Complexity

- Time: O(1)

- Space:O(1)

# Results

Python)

Runtime
39 ms
Beats
49.53%
Memory
16.3 MB
Beats
48.1%

Rust)

Runtime
0 ms
Beats
100%
Memory
2 MB
Beats
71.43%