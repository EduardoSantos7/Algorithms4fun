import "math"

func maxLengthBetweenEqualCharacters(s string) int {
    mem := make(map[rune]int)
    possible_substring := false
    max_substring_len := 0
    
    for i, char := range s {
        if pos, found := mem[char]; found {
            possible_substring = true
            max_substring_len = int(math.Max(float64(max_substring_len), float64(i - pos - 1)))
        } else {
            mem[char] = i
        }
    }
    
    if possible_substring {
        return max_substring_len
    }
    
    return -1
}
