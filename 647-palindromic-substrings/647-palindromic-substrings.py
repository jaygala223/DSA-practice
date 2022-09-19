class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = len(s)
        
        for i in range(len(s)):
            #odd len#
            l,r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
            #even len#
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
        return ans