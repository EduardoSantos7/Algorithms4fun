class Solution {
    fun balancedStringSplit(s: String): Int {
        var count = 0
        var res = 0

        s.forEach {
            if (it == 'R') {
                count += 1
            } else {
                count -= 1
            }

            if (count == 0) {
                res += 1
            }
        }

        return res
    }
}
