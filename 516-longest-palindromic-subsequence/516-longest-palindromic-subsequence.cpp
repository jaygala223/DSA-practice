class Solution {
public:
    int lcs(string text1, string text2) {
        int n1 = text1.size();
        int n2 = text2.size();
        
        vector<vector<int>> dp(n1+1, vector<int>(n2+1, -1));
        
        for(int j=0; j<=n2; j++) dp[0][j] = 0;
        for(int i=0; i<=n1; i++) dp[i][0] = 0;
        
        for(int ind1=1; ind1<=n1; ind1++){
            for(int ind2=1; ind2<=n2; ind2++){
                
                //match
                if(text1[ind1-1] == text2[ind2-1]) {
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1];
                } 
                    
                //not match then
                else dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1]);
            }
        }
        
        return dp[n1][n2];
    }
    
    int longestPalindromeSubseq(string s) {
        string s2 = s;
        reverse(s2.begin(), s2.end());
        return lcs(s, s2);
    }
};