This file aims to help to remember in which circunstance every data structure/algorithm is useful and how it's used.

**Array**
---

**Monotonic Stack**: It is a type of stack used to keep elements in a sorted order (either increasing or decreasing) as you iterate through a list. The "monotonic" property means the values are either non-increasing or non-decreasing within the stack, which helps in solving problems that involve finding next greater or smaller elements, or where such relationships impact the problem's logic.

Think of a monotonic stack as a smart stack that helps you keep track of previous elements in a way that you can easily and quickly compare them to current or future elements. It's like having a list of elements sorted in a specific order, where you only add an element if it fits this order, and if it doesn't, you process and remove some elements until it does.

**When to Use a Monotonic Stack**

Monotonic stacks are particularly useful in scenarios such as:

**Next Greater Element**: To find the next greater element for each element in an array. If you're looking for the next greater element, you maintain a decreasing stack.
**Next Smaller Element**: Similarly, to find the next smaller element for each element in an array. Here, an increasing stack is maintained.
**Largest Rectangle in Histogram**: To calculate the largest possible rectangle in a histogram, where the height of each bar is given. You can use a stack to keep track of bars and calculate the area efficiently when you encounter a shorter bar.
**Trapping Rain Water**: Helps in calculating how much water can be trapped between bars in a histogram-like structure by using a stack to keep track of walls.
**Stock Span Problem**: To find the number of consecutive days before the current day where the stock price was less than or equal to the price on the current day.

**How It Works**
Here’s a general way on how a monotonic stack is typically used:

1) Initialize an empty stack.
2) Iterate through the elements: For each element, you repeatedly compare it with the element at the top of the stack.
3) Adjust the stack based on the condition:
    - If the current element should not be in the stack based on the monotonic condition (e.g., it breaks the increasing or decreasing order), pop elements from the stack. Often, you will perform some calculations or update your results when popping.
    - Push the current element (or its index) onto the stack after handling the above conditions.
4) Final processing: Sometimes, after iterating through all elements, you might need to process the elements still in the stack.

Example:

- Leetcode/1475. Final Prices With a Special Discount in a Shop

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