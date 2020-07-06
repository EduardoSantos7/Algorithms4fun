package main

type SpecialArray []interface{}

// Tip: Each element of `array` can either be cast
// to `SpecialArray` or `int`.
func ProductSum(array []interface{}) int {
	// Write your code here.
	return ProductSumHelper(array, 1)
}

func ProductSumHelper(array []interface{}, level int) int {
	total := 0
	for _, elem := range array {
		if cast, ok := elem.(SpecialArray); ok {
			total += ProductSumHelper(cast, level+1)
		} else if cast, ok := elem.(int); ok {
			total += cast
		}
	}
	return total * level
}
