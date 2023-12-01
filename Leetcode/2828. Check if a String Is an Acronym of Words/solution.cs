public class Solution {
    public bool IsAcronym(IList<string> words, string s) {
        return string.Join("", words.Select(word => word[0])) == s;
    }
}