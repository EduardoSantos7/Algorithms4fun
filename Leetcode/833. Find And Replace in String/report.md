# Algorithm Idea

We sort our replacement jobs (i, x, y) in reverse order. If S[i:].startswith(x), then we can replace that section S[i:i+len(x)] with the target y. We used a reverse order so that edits to S do not interfere with the rest of the queries

# Complexity

- Time: O(NQ) -> where NN is the length of S, and we have QQ replacement operations. (Our complexity could be faster with a more accurate implementation, but it isn't necessary.)

- Space:O(N)

# Results

Python)

    - Runtime: 68 ms, faster than 11.35% of Python3 online submissions for Find And Replace in String.

    - Memory Usage: 13.9 MB, less than 50.53% of Python3 online submissions for Find And Replace in String.
