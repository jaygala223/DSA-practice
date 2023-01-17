class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #https://www.youtube.com/watch?v=dw79Uf4s3cA
        #https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/3061225/Python-3-oror-7-lines-w-explanation-and-example-oror-TM%3A-100-96
        ans, ones = 0, 0
        
        for c in s:
            if c == '1':
                ones += 1
            else:
                ans = min(ans+1, ones)
        
        return ans