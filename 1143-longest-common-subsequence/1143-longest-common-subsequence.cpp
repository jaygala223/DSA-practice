class Solution {
public:
    int f(int ind1, int ind2, string s1, string s2, vector<vector<int>> &dp){
        if(ind1 < 0 || ind2 < 0) return 0;
        if(dp[ind1][ind2] != -1) return dp[ind1][ind2];
        //if match then add to lcs ans
        if(s1[ind1] == s2[ind2]) 
            return dp[ind1][ind2] = 1 + f(ind1-1, ind2-1, s1, s2, dp);
        
        //not match then
        return dp[ind1][ind2] = max(f(ind1-1, ind2, s1, s2, dp), f(ind1, ind2-1, s1, s2, dp));
    }
    
    
    int longestCommonSubsequence(string text1, string text2) {
        int n1 = text1.size();
        int n2 = text2.size();
        
        vector<vector<int>> dp(n1+1, vector<int>(n2+1, -1));
        
        for(int j=0; j<=n2; j++) dp[0][j] = 0;
        for(int i=0; i<=n1; i++) dp[i][0] = 0;
        
        for(int ind1=1; ind1<=n1; ind1++){
            for(int ind2=1; ind2<=n2; ind2++){
                
                //match
                if(text1[ind1-1] == text2[ind2-1]) dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]; 
                    
                //not match then
                else dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1]);
            }
        }
        
        return dp[n1][n2];
    }
};