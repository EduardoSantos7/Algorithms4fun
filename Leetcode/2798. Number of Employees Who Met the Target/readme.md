# Algorithm Idea

Traverse the list and check every element. Comparing if it's greater or equal to the target. If it's then increase a coutner variable. Return the counter.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Typescript)

Runtime
57 ms
Beats
80%
Memory
44.5 MB
Beats
56.39%

Python)

Runtime
48 ms
Beats
58.74%
Memory
16.1 MB
Beats
96.61%

Rust)

Runtime
0 ms
Beats
100%
Memory
2.1 MB
Beats
53.85%

Go)

Runtime
3 ms
Beats
62.80%
Memory
2.7 MB
Beats
94.82%

C#)

public class Solution {
public int NumberOfEmployeesWhoMetTarget(int[] hours, int target) {
return hours.Where(h => h >= target).Count();
}
}
