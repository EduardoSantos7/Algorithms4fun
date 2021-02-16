func firstUniqChar(s string) int {
    count := make(map[rune]int)
    
    for _, char := range s {
        _, ok := count[char]
        
        if ok {
            count[char] += 1
        } else {
            count[char] = 1
        }  
    }
    
    for i, char := range s {
        val, _ := count[char]
        
        if val == 1 {
            return i
        }
    }
    
    return -1
}