func replaceElements(arr []int) []int {
	if len(arr) == 1 {
		result := []int{-1}
		return result
	}

	for i := 0; i < len(arr)-1; i++ {
		arr[i] = max(arr[i+1:])
	}

	arr[len(arr)-1] = -1
	return arr
}

func max(array []int) int {
	var max int = array[0]
	for _, value := range array {
		if max < value {
			max = value
		}
	}
	return max
}