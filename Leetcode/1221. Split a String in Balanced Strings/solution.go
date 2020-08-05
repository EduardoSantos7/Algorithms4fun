func balancedStringSplit(s string) int {
    count := 0
    res := 0
    
    for _, char := range s {
        if char == 'R' {
            count += 1
        } else {
            count -= 1
        }
        
        if count == 0 {
            res += 1
        }
    }
    
    return res
}