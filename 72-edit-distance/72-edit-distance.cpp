class Solution {
public:
    int f(int ind1, int ind2, string &s1, string &s2, vector<vector<int>> &dp){
        if(ind1 < 0) return ind2+1;
        if(ind2 < 0) return ind1+1;
        if(dp[ind1][ind2] != -1) return dp[ind1][ind2];
        
        //agar matched
        if(s1[ind1] == s2[ind2]) return f(ind1-1, ind2-1, s1, s2, dp);
        
        //not match
        return dp[ind1][ind2] = 1 + min(f(ind1-1, ind2, s1, s2, dp), min(f(ind1, ind2-1, s1, s2, dp), f(ind1-1, ind2-1, s1, s2, dp)));
    }
    
    int minDistance(string word1, string word2) {
        if(word1 == word2) return 0;
        
        int n1 = word1.size();
        int n2 = word2.size();
        
        vector<vector<int>> dp(n1+1, vector<int> (n2+1, 0));
        
        
        //if(ind1 < 0) return ind2+1;
        //if(ind2 < 0) return ind1+1;
        for(int ind1=0; ind1<=n1; ind1++) dp[ind1][0] = ind1;
        for(int ind2=0; ind2<=n2; ind2++) dp[0][ind2] = ind2;
        
        for(int ind1=1; ind1<=n1; ind1++){
            for(int ind2=1; ind2<=n2; ind2++){
                if(word1[ind1-1] == word2[ind2-1]) dp[ind1][ind2] = dp[ind1-1][ind2-1];
        
                //not match
                else{
                    int op1 = 1e8, op2 = 1e8, op3 = 1e8;
                    op1 = dp[ind1-1][ind2];
                    op2 = dp[ind1][ind2-1];
                    op3 = dp[ind1-1][ind2-1];

                    dp[ind1][ind2] = 1 + min(op1, min(op2, op3));    
                }
                
            }
        }
        
        return dp[n1][n2];
        //return f(n1-1, n2-1, word1, word2, dp);
    }
};