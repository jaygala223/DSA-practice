class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        occurences = {}
        
        left, right, ans = 0, 0, 0
        n = len(s)
        
        while left < n and right < n:
            if s[right] in occurences:
                left = max(left, occurences[s[right]] + 1)
            
            occurences[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans