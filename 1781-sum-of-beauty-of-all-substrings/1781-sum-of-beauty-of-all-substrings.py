class Solution:
    def beautySum(self, s: str) -> int:
        
        ans = 0
        
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                
                mini = 1000
                maxi = 0
                
                for item in freq:
                    mini = min(mini, freq[item])
                    maxi = max(maxi, freq[item])
                ans += maxi - mini
        
        return ans
        