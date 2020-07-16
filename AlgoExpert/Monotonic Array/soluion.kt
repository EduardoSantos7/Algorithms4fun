package com.algoexpert.program

fun isMonotonic(array: List<Int>): Boolean {
    if (array.size < 2) { return true }

    var trend = 0
    var is_increasing = 0

    for (i in 1..array.size - 1) {
        if (array[i] == array[i - 1]) { continue }

        if (array[i] > array[i - 1]) {
            is_increasing = 1
        } else {
            is_increasing = -1
        }

        if (trend == 0) {
            trend = is_increasing
            continue
        }

        if (trend != is_increasing) { return false }
    }

    return true
}
