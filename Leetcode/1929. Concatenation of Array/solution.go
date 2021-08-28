func getConcatenation(nums []int) []int {
    var (
        n = len(nums)
        ans = make([]int, n+n)
    )

    for i, num := range nums {
        ans[i] = num
        ans[i+n] = num
    }

    return ans
}