def firstDuplicateValue(array):
    for elem in array:
		abs_elem = abs(elem)
		if array[abs_elem - 1] < 0:
			return abs_elem
		array[abs_elem - 1] *= -1
	return -1
