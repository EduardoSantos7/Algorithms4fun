func arithmeticTriplets(nums []int, diff int) int {
    var ans = 0
    var seen = make(map[int]bool)

    for _, num := range nums {
        if seen[num - diff] && seen[num - diff - diff] {
            ans += 1
        } 
        seen[num] = true
    }

    return ans
}