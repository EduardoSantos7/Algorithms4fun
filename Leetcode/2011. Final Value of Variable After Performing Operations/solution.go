import ("strings");


func finalValueAfterOperations(operations []string) int {
    acum := 0
    
    for _, op := range(operations) {
        if strings.Contains(op, "+") {
            acum += 1
        } else {
            acum -= 1
        }
    }
    
    return acum
}