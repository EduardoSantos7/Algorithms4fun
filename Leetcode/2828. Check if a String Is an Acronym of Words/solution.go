func isAcronym(words []string, s string) bool {
    var initials string
    for _, word := range words {
        initials += string(word[0])
    }
    return initials == s
}