class Solution {
public:
    bool f(int i, int j, int k, string &s1, string &s2, string &s3, vector<vector<int>> &dp){
        if(i == s3.size()) return 1;
        if(dp[j][k] != -1) return dp[j][k];
        
        int first = 0; 
        int second = 0;
        if(j < s1.size() and s3[i] == s1[j]) first = f(i+1, j+1, k, s1, s2, s3, dp);
        if(k < s2.size() and s3[i] == s2[k]) second = f(i+1, j, k+1, s1, s2, s3, dp);
        
        return dp[j][k] = (first || second);
    }
    
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size();
        int m = s2.size();
        int len = s3.size();
        
        vector<vector<int>> dp(n+1, vector<int>(m+1,-1));
        
        if(len != n + m) return false;
        
        
        
        return f(0, 0, 0, s1, s2, s3, dp);
    }
};