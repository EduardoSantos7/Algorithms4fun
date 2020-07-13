package com.algoexpert.program

fun moveElementToEnd(array: MutableList<Int>, toMove: Int): List<Int> {
    // Write your code here.
	var keep = 0
	
	for (runner in 0..array.size - 1) {
		if (array[runner] == toMove) {
			continue
		}
		val temp = array[keep]
		array[keep] = array[runner]
		array[runner] = temp
		keep += 1
	}
    return array
}
