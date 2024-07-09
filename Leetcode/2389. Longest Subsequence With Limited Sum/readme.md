# Algorithm Idea

Approach 1)

The algorithm begins by sorting the input list nums. This sorting ensures that when sums are computed to answer queries, smaller numbers are considered first, potentially allowing for larger subsets of numbers that sum to values not exceeding the queries. For each query, the algorithm initializes a sum accumulator acum and iterates through the sorted nums list, adding each number to acum until the sum exceeds the query value. The number of elements added before exceeding the query is stored as the result for that query.

Approach 2)

The first step involves sorting the input array. Once the array is sorted, the next step is to compute the cumulative sums of these elements. This cumulative sum array, often called a prefix sum array, is created such that each element at index i in this new array represents the sum of all elements in the original array from the start up to and including the element at index i. This array can be constructed in a linear pass, where each new element is the sum of the previous element in the prefix sum array and the current element in the sorted array.

With the prefix sum array prepared, the problem of determining how many elements can be summed without exceeding a specific value (query) translates to finding the largest sum in the prefix sum array that is less than or equal to the query. Binary search is utilized here because the prefix sum array is sorted by construction.

The main difference between the two approaches lies in how they handle the summation and search operations:

Approach 1 manually computes the cumulative sums for each query and checks each sum incrementally until the sum exceeds the query. This method can be inefficient because it repeatedly sums elements for each query.

Approach 2 efficiently computes all cumulative sums once and utilizes a binary search (bisect_right) to quickly find the point at which the sum exceeds each query. This reduces the computational overhead by avoiding repeated summation and leverages faster searching through sorted data.


# Complexity

Approach 1)

- Time: O(N*M)

- Space:O(M)
  
Approach 2)

- Time: O(N*LogN)

- Space:O(N)

# Results

Approach 1)

Runtime
259
ms
Beats
19.23%

Memory
16.91
MB
Beats
24.75%

Approach 2)

Runtime
82
ms
Beats
90.99%

Memory
16.78
MB
Beats
92.13%
