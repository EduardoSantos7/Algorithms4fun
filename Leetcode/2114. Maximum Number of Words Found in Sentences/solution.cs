public class Solution {
    public int MostWordsFound(string[] sentences) {
        int MaxWords = 0;
        
        foreach(string sentence in sentences)
        {
            MaxWords = Math.Max(MaxWords, sentence.Split(" ").Length);
        }
        
        return MaxWords;
    }
}