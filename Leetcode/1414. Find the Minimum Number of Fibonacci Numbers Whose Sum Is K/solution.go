func findMinFibonacciNumbers(k int) int {
    fibs := make([]int, 0)
    fibs = append(fibs, 1)
    fibs = append(fibs, 1)
    
    for fibs[len(fibs) - 1] < k {
        fibs = append(fibs, fibs[len(fibs) - 1] + fibs[len(fibs) - 2])
    }
    
    count := 0
    res := 0
    
    for i := len(fibs) - 1; i >= 0; i-- {
        if fibs[i] + count < k { 
            count += fibs[i] 
            res++
        } else if fibs[i] + count == k{ 
            res++;
            break
        }
    }
    return res
}