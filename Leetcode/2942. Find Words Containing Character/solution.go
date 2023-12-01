func findWordsContaining(words []string, x byte) []int {

    var ans []int

    for index, word := range words {
        if strings.IndexByte(word, x) == -1 {
            continue
        }

        ans = append(ans, index)
    }

    return ans
}