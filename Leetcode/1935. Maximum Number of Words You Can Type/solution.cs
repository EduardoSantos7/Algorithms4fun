public class Solution {
    public int CanBeTypedWords(string text, string brokenLetters) {
        var result = 0;
        var hasBrokenLetters = false;
        var brokenSet = new HashSet<char>(brokenLetters);

        foreach(var c in text)
        {
            if(c == ' ')
            {
                if(hasBrokenLetters)
                {
                    hasBrokenLetters = false;
                    continue;
                }

                result += 1;
            }

            if(brokenSet.Contains(c)) hasBrokenLetters = true;
        }

        return hasBrokenLetters ? result : result + 1;
    }
}