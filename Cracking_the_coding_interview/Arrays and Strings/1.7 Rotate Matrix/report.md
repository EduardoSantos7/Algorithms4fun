# Problem

Given an image represented by N X N matrix, where each pixe in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?

# Algorithm Idea

Move the top edge to right edge, the righ to the bottom, the bottom to the left and left to the top edge. This should be done for each layer. There are N/2 layers where the N is the lenght of a row/column

# Complexity

- Time: O(N^2)

- Space:O(1)
