# Algorithm Idea

Certainly! The code implements an algorithm that counts the number of binary substrings with an equal number of 0s and 1s.

**Algorithm Description**:

1. **Initialization**:
   - Use three counters:
     - `curr` which counts the current run of the same number (initialized to 1 because we start examining from the second character of the string),
     - `prev` which counts the previous run of numbers (initialized to 0),
     - `ans` which accumulates the answer (also initialized to 0).

2. **Iterate over the string**:
   - Start iterating from the second character (i.e., index 1).
   - For each character in the string, compare it with the previous character.
     - If they are the same, increment the `curr` counter.
     - If they differ:
       - Increment the answer (`ans`) by the minimum of `curr` and `prev` (because that's the maximum number of valid binary substrings ending at that position which can be formed).
       - Move the value of `curr` to `prev` (i.e., the current run length becomes the previous run length for the next iteration).
       - Reset `curr` to 1 since we're starting a new run of characters.

3. **Final Accumulation**:
   - Once the string iteration is complete, there might be a possibility of forming more valid binary substrings at the end of the string. Hence, increment the answer (`ans`) by the minimum of the current (`curr`) and previous (`prev`) run lengths.

4. **Return the Result**:
   - The `ans` variable now contains the count of the non-empty binary substrings in the string `s` that have an equal number of 0's and 1's. Return this value.

**Example**:
For a clearer understanding, let's consider a small example, `s = "00110011"`. 
- `curr` will count the continuous occurrence of a number (either 0 or 1).
- `prev` will hold the count of the last continuous occurrence when a change from 0 to 1 or vice versa is noticed.

Steps:
1. Initialize `curr = 1`, `prev = 0`, `ans = 0`.
2. Start from the second character.
   - For `i=1`, `s[i] = 0` (same as `s[i-1]`), so `curr=2`.
   - For `i=2`, `s[i] = 1` (not same as `s[i-1]`), so `ans` increases by `min(2,0) = 0`. Then, `prev` is set to 2 and `curr` is reset to 1.
   - For `i=3`, `s[i] = 1` (same as `s[i-1]`), so `curr=2`.
   - For `i=4`, `s[i] = 0` (not same as `s[i-1]`), so `ans` increases by `min(2,2) = 2`. Then, `prev` becomes 2, and `curr` is reset to 1.
   - … (continuing this way)
3. By the end, `ans` is 6 (substrings: "0011", "01", "1100", "10", "0011", and "01").

Thus, the algorithm efficiently counts the valid binary substrings by tracking consecutive occurrences of the numbers.

# Complexity

- Time: O(n)

- Space:O(1)

# Results

Runtime
0 ms
Beats
100%
Memory
2.3 MB
Beats
83.33%