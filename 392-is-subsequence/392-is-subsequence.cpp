class Solution {
public:
    bool isSubsequence(string s, string t) {
        //int n = s.length(), m=t.length();
        int j = 0; 
    
        for (int i = 0; i < t.length() and j < s.length(); i++)
            if (s[j] == t[i]) j++;
        
    return (j == s.size());
    }
};