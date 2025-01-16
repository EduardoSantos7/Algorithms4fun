public class Solution {
    public int MinimumPushes(string word) {
        int i = 0; int res = 0;

        for (int j = 0; j < word.Length; j++)
        {
            if ((j) % 8 == 0) i++;
            res += i;
        }

        return res;
    }
}