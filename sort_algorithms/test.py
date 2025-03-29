import pytest
import time
from sort_algorithms.sorter import Sorter

# FILE: sort_algorithms/test_test.py


@pytest.mark.parametrize("sort_algorithm", [
    # Add your sort algorithm implementations here
    # Example: bubble_sort, quick_sort, merge_sort
    "bubble_sort"
])
def test_sort_algorithm(sort_algorithm):
    sorter = Sorter(sort_algorithm)
    
    # Test data
    data = [5, 3, 8, 6, 2, 7, 4, 1]
    expected = sorted(data)
    
    # Measure time
    start_time = time.time()
    result = sorter.sort(data)
    end_time = time.time()
    
    # Check if the result is sorted correctly
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # Print the length of elements sorted and time taken
    print(f"Length of elements sorted: {len(data)}")
    print(f"Time taken: {end_time - start_time} seconds")

# @pytest.mark.parametrize("sort_algorithm", [
#     # Add your sort algorithm implementations here
#     # Example: bubble_sort, quick_sort, merge_sort
# ])
# def test_sort_algorithm_stability(sort_algorithm):
#     sorter = Sorter(sort_algorithm)
    
#     # Test data with duplicate values
#     data = [(5, 'a'), (3, 'b'), (8, 'c'), (6, 'd'), (2, 'e'), (7, 'f'), (4, 'g'), (1, 'h'), (3, 'i')]
#     expected = sorted(data, key=lambda x: x[0])
    
#     # Measure time
#     start_time = time.time()
#     result = sorter.sort(data, key=lambda x: x[0])
#     end_time = time.time()
    
#     # Check if the result is sorted correctly and stable
#     assert result == expected, f"Expected {expected}, but got {result}"
    
#     # Print the length of elements sorted and time taken
#     print(f"Length of elements sorted: {len(data)}")
#     print(f"Time taken: {end_time - start_time} seconds")