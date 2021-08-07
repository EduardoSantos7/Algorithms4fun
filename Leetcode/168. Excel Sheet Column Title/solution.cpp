class Solution {
public:
    string convertToTitle(int columnNumber) {
        string s = "";
        int j,n = columnNumber;
        if(columnNumber <= 26) {
            s = columnNumber + 64;
            return s;
        }
        
        while(n != 0) {
            if(n % 26 == 0) {
                s += 'Z';
                n--;
            } else {
                if (n > 26) {
                    j = n % 26;
                } else{
                    j = n;
                }
            
                s += j + 64;
            }
            
            if(n <= 26) break;
            
            n /= 26;
        }
        
        reverse(s.begin(), s.end());
        return s;
        
    }
};