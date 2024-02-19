This file aims to help to remember in which circunstance every data structure/algorithm is useful and how it's used.

**Array + Hashmap**
---

When given an array, a hash map can be used to:

- Group the elements of the array or its indexes into buckets, this is useful to have some kind of sort.
- Count the frequency of each element in the array

A lot of the utility of the hash map when dealing with arrays is to decrease the time complexity for cuadratic to linear, but this usually means to increase the memory complexity to a linear.

Examples:

* Frequency:
  - Leetcode/2610
* Buckets:
  - Leetcode/1282