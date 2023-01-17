class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        zeros, ones, ans = 0, 0, 0
        
        for char in s:
            if char == '1':
                ones += 1
            else:
                zeros += 1
            zeros = min(zeros, ones)
        
        return zeros