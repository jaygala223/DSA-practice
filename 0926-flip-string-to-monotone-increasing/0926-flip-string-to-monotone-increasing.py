class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        ans, ones = 0, 0
        
        for c in s:
            if c == '1':
                ones += 1
            else:
                ans = min(ans+1, ones)
        
        return ans