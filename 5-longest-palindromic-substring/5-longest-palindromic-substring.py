class Solution:
    def longestPalindrome(self, s: str) -> str:
        ansLen = 0
        l_final, r_final = 0,0
        
        for i in range(len(s)):
            
            #odd len
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l + 1 > ansLen:
                    ansLen = r-l + 1
                    l_final, r_final = l, r
                    #because it stores a copy everytime and thus O(n^3)
                    #res = s[l:r+1]
                l -= 1
                r += 1
                
            
            
            #even len
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l + 1 > ansLen:
                    ansLen = r-l + 1
                    l_final, r_final = l, r
                    #res = s[l:r+1]
                l -= 1
                r += 1
            
        return s[l_final:r_final+1]
            