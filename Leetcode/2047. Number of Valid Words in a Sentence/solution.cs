public class Solution {
    public int CountValidWords(string sentence) {
        int validWords = 0;
        var words = sentence.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string word in words) {
            bool isValid = true;
            bool hyphenAlreadyPresent = false;
            bool punctuationAlreadyPresent = false;
            int n = word.Length;

            for (int i = 0; i < n; i++) {
                char c = word[i];

                if (char.IsDigit(c)) {
                    isValid = false;
                    break;
                }

                if (c == '-') {
                    if (hyphenAlreadyPresent || i == 0 || i == n - 1 || !char.IsLower(word[i - 1]) || !char.IsLower(word[i + 1])) {
                        isValid = false;
                        break;
                    }
                    hyphenAlreadyPresent = true;
                }

                if (c == '!' || c == '.' || c == ',') {
                    if (punctuationAlreadyPresent || i != n - 1) {
                        isValid = false;
                        break;
                    }
                    punctuationAlreadyPresent = true;
                }
            }

            if (isValid) validWords++;
        }

        return validWords;
    }
}