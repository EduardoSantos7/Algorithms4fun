# Algorithm Idea

The manner in which we add money is static. Each week we add:

1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
3 + 4 + 5 + 6 + 7 + 8 + 9 = 42
and so on...

We have k = n / 7 full weeks. Here, we are performing integer/floor division. These full weeks form an arithmetic sequence. An arithmetic sequence is a sequence of numbers such that the difference between every adjacent element is the same. Here, we have a common difference of 7.

The sum of an arithmetic sequence can be found very quickly if we know the following information:

The first element in the sequence FFF.
The final element in the sequence LLL.
The number of elements in the sequence kkk.
Then, the sum is (k*(F+L))/2
2
k⋅(F+L)
​
We know the first element in the sequence is 28 and that there are k elements in the sequence, since each element represents a week. What is the final element in the sequence? The final element in the sequence represents how much money we add in the final full week, and we know that the value must be 28 + (k - 1) * 7, since we add 28 dollars on the first week and 7 more dollars each additional week.

Let F = 28, k = n / 7, L = 28 + (k - 1) * 7. We can then plug each of these values into the above equation to get the total money we deposit in all full weeks as arithmeticSum.

What if n is not divisible by 7? Then, the final week will have less than 7 days. How do we calculate how much money we get from the final week? First, we need to know how many days are in the final week. We can obtain this by taking n modulo 7, i.e. n % 7.

Note that we will have k full weeks before the final week, therefore, on the Monday of the final week, we will deposit 1 + k dollars. We can either form another arithmetic sequence for the final week (since we know its first value and how many elements there will be, we can deduce the final value and thus the overall sum), or we could simply iterate over the final week explicitly.

For the sake of simplicity, we will iterate over the final week explicitly and calculate the money we deposit as finalWeek.

Finally, the answer to the problem is arithmeticSum + finalWeek.

# Complexity

- Time: O(1)

- Space:O(1)

# Results

Runtime
23
ms
Beats
99.29%
of users with Python3

Memory
16.63
MB
Beats
13.56%
of users with Python3