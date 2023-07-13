# Algorithm Idea

These three cases are possible with string aaa and bbb:-

a=ba=ba=b. If both the strings are identical, it is obvious that no subsequence will be uncommon. Hence, return -1.

length(a)=length(b)length(a)=length(b)length(a)=length(b) and a≠ba \ne ba

=b. Example: abcabcabc and abdabdabd. In this case we can consider any string i.e. abcabcabc or abdabdabd as a required subsequence, as out of these two strings one string will never be a subsequence of other string. Hence, return length(a)length(a)length(a) or length(b)length(b)length(b).

length(a)≠length(b)length(a) \ne length(b)length(a)

=length(b). Example abcdabcdabcd and abcabcabc. In this case we can consider bigger string as a required subsequence because bigger string can't be a subsequence of smaller string. Hence, return max(length(a),length(b))max(length(a),length(b))max(length(a),length(b)).

# Complexity

- Time: O(min(x,y))O(min(x,y))O(min(x,y)). where xxx and yyy are the lengths of strings aaa and bbb respectively. Here equals method will take min(x,y)min(x,y)min(x,y) time .

- Space: O(1)O(1)O(1). No extra space required.

# Results

Runtime
52 ms
Beats
22.57%
Memory
16.4 MB
Beats
31.88%