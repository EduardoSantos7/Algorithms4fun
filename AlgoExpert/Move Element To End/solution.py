def moveElementToEnd(array, toMove):
    runner = 0
    keep = 0
    for _ in range(len(array)):
        if array[runner] == toMove:
            runner += 1
            continue
        # Swap
        array[runner], array[keep] = array[keep], array[runner]
        keep += 1
        runner += 1

    return array
