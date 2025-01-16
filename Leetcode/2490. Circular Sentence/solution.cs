public class Solution {
    public bool IsCircularSentence(string sentence) {
        if (sentence[0] != sentence[sentence.Length - 1]) { return false; }

        for (int i = 1; i < sentence.Length; i++)
        {
            if (sentence[i] == ' ' && sentence[i-1] != sentence[i+1]) { return false; }
        }

        return true;
    }
}