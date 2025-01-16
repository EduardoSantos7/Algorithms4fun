public class Solution {
    public bool MakeEqual(string[] words) {
        Dictionary<char, int> freq = new();

        foreach(string word in words)
        {
            foreach(var c in word)
            {
                freq.TryGetValue(c, out var count);
                freq[c] = count > 0 ? count + 1 : 1;
            }
        }

        var numberOfWords = words.Count();
        var freqValues = freq.Values;

        for(int i = 0; i < freq.Count(); i ++)
        {
            if (freqValues.ElementAt(i) % numberOfWords != 0)
            {
                return false;
            }
        }

        return true;
    }
}