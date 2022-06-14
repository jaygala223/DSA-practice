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
    
    int minDistance(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        
        vector<vector<int>> dp(n1+1, vector<int>(n2+1, -1));
        
        int lcs = f(n1-1, n2-1, word1, word2, dp);
        cout<<lcs;
        return n1 + n2 - 2*lcs;
    }
};