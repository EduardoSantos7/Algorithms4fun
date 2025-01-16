public class Solution
{
    public int MinimumPushes(string word) =>
        (1 + (word.Length >> 3)) * (((word.Length >> 3) << 2) + (word.Length & 7));
}