class Solution:
    dp = [-1]*46
    
    def climbStairs(self, n: int) -> int:
        if n<=1: return 1
        if self.dp[n] != -1: return self.dp[n]
        
        left = self.climbStairs(n-1)
        right = self.climbStairs(n-2)
        
        self.dp[n] = left+right
        return self.dp[n]