def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    p1 = 0
    p2 = 0
    smallest = float('inf')
    smallest_pair = []

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        num1, num2 = arrayOne[p1], arrayTwo[p2]

        if num1 < num2:
            current = num2 - num1
            p1 += 1
        elif num2 < num1:
            current = num1 - num2
            p2 += 1
        else:
            return [num1, num2]

        if smallest > current:
            smallest = current
            smallest_pair = [num1, num2]

    return smallest_pair
