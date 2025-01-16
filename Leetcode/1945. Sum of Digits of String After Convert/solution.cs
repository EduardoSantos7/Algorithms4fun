public class Solution {
    public int GetLucky(string s, int k) {
        int res = 0;

        foreach(var c in s)
        {
            var val = c - 'a' + 1;
            res += val % 10;
            res += val /= 10;
        }

        while (--k > 0)
        {
            var n = res;
            res = 0;

            while (n > 0)
            {
                res += n % 10;
                n /= 10;
            }
        }

        return res;
    }
}