func rob(nums []int) int {
    a, b, temp := 0, 0, 0
    
    for _, num := range(nums) {
        if a + num > b {
            temp = a + num
        } else {
            temp = b
        }
        a = b
        b = temp
    }
    
    return b
}