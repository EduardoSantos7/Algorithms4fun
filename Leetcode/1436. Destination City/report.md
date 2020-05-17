# Algorithm Idea

**Brute Force**

Traverse the list and save both cities in a `dict` tag the start city for example with a `s` and the end city just with `None` if it doesn't exist in the `dict` and at the end traverse the `dict` to detect which value has a `None`, that's tthe value we want to return.

**Sets**

We can create 2 `sets`, one for the start cities and another for end cities, by the end we will return the substraction oof `end_cities - start_cities`

# Complexity

Both algorithms)

- Time: O(N)

- Space:O(N)

# Results

Brute Force)

    Python)

        - Runtime: 48 ms, faster than 95.43% of Python3 online submissions for Destination City.

        - Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Destination City.
    
    Go)

        - Runtime: 4 ms, faster than 92.19% of Go online submissions for Destination City.

        - Memory Usage: 4.3 MB, less than 100.00% of Go online submissions for Destination City.
    
Sets)

    Python)

        - Runtime: 48 ms, faster than 95.43% of Python3 online submissions for Destination City.

        - Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Destination City.
    
    Go)

        - Runtime: 0 ms, faster than 100.00% of Go online submissions for Destination City.

        - Memory Usage: 3.9 MB, less than 100.00% of Go online submissions for Destination City.