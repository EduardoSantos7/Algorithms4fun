# Algorithm Idea

Create a hashmap for each list where store the index value, then iterate the smaller list checking if the restaurant is in the other list, if that happens add it to a third hashmap saving the sum of both indexes then find the minimum value in the third hashmap and filter the restaurants with the same value.

# Complexity

- Time: O(n) - Make the hashmaps and iterate the smaller one, also get the min and filter.

- Space:O(n) - The strings saved in the map

# Results

Python)

- Runtime: 148 ms, faster than 91.83% of Python3 online submissions for Minimum Index Sum of Two Lists.

- Memory Usage: 14.9 MB, less than 39.83% of Python3 online submissions for Minimum Index Sum of Two Lists.
