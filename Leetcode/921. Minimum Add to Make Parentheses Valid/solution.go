func minAddToMakeValid(S string) int {
    stack := make([]int, 0)
    
    for _, char := range S {
        if len(stack) > 0 && stack[len(stack) - 1] == '(' && char == ')' {
            stack = stack[:len(stack) - 1]
        } else {
            stack = append(stack, int(char))
        }
    }
    
    return len(stack)
}