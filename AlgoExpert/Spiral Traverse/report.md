# Algorithm Idea

You can think of the spiral that you have to traverse as a set of rectangle perimeters that progressively get smaller (i.e., that progressively move inwards in the two-dimensional array). Declare four variables: a starting row, a starting column, an ending row, and an ending column. These four variables represent the bounds of the first rectangle perimeter in the spiral that you have to traverse. Traverse that perimeter using those bounds, and then move the bounds inwards. End your algorithm once the starting row passes the ending row or the starting column passes the ending column.

# Complexity

- Time: O(N) - Where N is the number of elements

- Space:O(1)

# Results
