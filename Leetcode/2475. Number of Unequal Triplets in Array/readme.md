# Algorithm Idea

The solution transforms the problem of finding distinct triplets into a problem of calculating combinations based on cumulative frequencies. Doing this avoids the need to review every possible combination of indexes in the array, which would be inefficient. Instead, the information on how many times each number appears and how these occurrences are distributed across the array is used to directly calculate the number of valid triplets.

Frequency Count:

Go through the list of numbers and calculate how many times each number appears. This can be stored in a data structure that associates each unique number with its frequency of occurrence (such as a dictionary or map).

Calculation of Cumulative Sums:

Create a list of cumulative sums of the frequencies of each unique number. This list will indicate how many numbers have been considered up to each point in the original list, counting each number according to its frequency.

Calculation of Combinations for Triplets:

It begins an iterative process where each step calculates the number of possible combinations of triplets whose elements are different from each other. For each item in the cumulative sums list (except the first and last):
    Consider the segment before this element as the total of possible options for the first number of the triplet.
    Consider the frequency of the current number as the options for the second number of the triplet.
    Consider the segment after this number as the options for the third number of the triplet.
Multiply these three quantities to obtain the number of possible triplets with the current number as the second element and add these results.

Approach 2)

Approach the counting in a slightly different manner, focusing on an incremental calculation involving a sliding consideration of left and right segments relative to the current number being processed.

Initialize the Counter and Variables:

c = Counter(nums): This counts the occurrences of each number in nums, similar to the previous algorithm.
res = 0: This initializes the result counter, which will accumulate the total number of valid triplets.
left = 0: This keeps track of the count of numbers (considered cumulatively) to the left of the current number.
right = len(nums): This initially sets to the total number of elements in nums and tracks the count of numbers to the right of the current number.
Iterate Over the Frequency Counts:

The loop iterates through each unique number's frequency:
right -= freq: Before processing each number, subtract its frequency from right because these occurrences will now either be in the left segment or being processed.
res += left * freq * right: Calculate the number of triplets for the current number. Here, left represents the number of options for nums[i], freq is the number of ways to pick the current number for nums[j], and right is the number of options for nums[k] after excluding all occurrences of the current number.
left += freq: After processing, add the frequency of the current number to left since it now forms part of the left segment for subsequent numbers.
Return the Result:

After all frequencies are processed, res holds the total number of valid triplets where nums[i], nums[j], and nums[k] are pairwise distinct.
Differences from the First Algorithm:
Incremental Update of left and right: Unlike the first algorithm, which precomputes a list of cumulative sums, this algorithm dynamically updates the left and right counters as it processes each unique number's frequency. This method can be more intuitive in terms of visualizing the triplet formation as moving through the list.
Direct Calculation Per Number: The second algorithm calculates the triplet count directly for each unique number based on its role as the middle number in the triplet, using left and right for the other two positions. The first algorithm instead calculates possibilities based on cumulative frequencies without explicitly moving a window through the list.

# Complexity

Approach 1)

- Time: O(n)

- Space:O(n)

Approach 2)

- Time: O(n)

- Space:O(n)

# Results

Approach 1)

Approach 2)