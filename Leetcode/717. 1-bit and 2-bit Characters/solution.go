func isOneBitCharacter(bits []int) bool {
    i := 0
    result := false

    for i < len(bits) {
        if bits[i] == 0 {
            result = true;
            i++
            continue
        }

        result = false
        i += 2
    }

    return result
}