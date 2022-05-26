class Solution {
public:
    
    vector<int> dp = vector<int>(46,-1);
    
    int climbStairs(int n) {
        if(n <= 1) return 1;
        if(dp[n] != -1) return dp[n];
        
        //left and right here mean the RECURSIVE TREE'S left and right
        
        int left = climbStairs(n-1);
        int right = climbStairs(n-2);
        
        dp[n] = left+right;
        return left+right;
    }
};