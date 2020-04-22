func replaceElements(arr []int) []int {
	if len(arr) == 1 {
		result := []int{-1}
		return result
	}

	index := 0
	currentMax := -1
	for i := 0; i < len(arr)-1; i++ {
		if i == index {
			currentMax, index = maxAndIndex(arr[i+1:])
			index += i + 1
		}
		arr[i] = currentMax
	}

	arr[len(arr)-1] = -1
	return arr
}

func maxAndIndex(array []int) (int, int) {
	var max int = array[0]
	var index = 0
	for i, value := range array {
		if max < value {
			max = value
			index = i
		}
	}
	return max, index
}