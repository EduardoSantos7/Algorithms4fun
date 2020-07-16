package main

func IsMonotonic(array []int) bool {
	if len(array) < 2 {
		return true
	}

	trend := 0
	is_increasing := 0

	for i := 1; i < len(array); i++ {
		if array[i] == array[i-1] {
			continue
		}

		if array[i] > array[i-1] {
			is_increasing = 1
		} else {
			is_increasing = -1
		}

		if trend == 0 {
			if is_increasing == 1 {
				trend = 1
			} else {
				trend = -1
			}
			continue
		}

		if trend != is_increasing {
			return false
		}
	}

	return true
}
