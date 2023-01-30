class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        if n == 2: return 1
        
        a, b, c = 0, 1, 1
        ans = 0
        
        for i in range(3, n+1):
            ans = a + b + c
            a = b
            b = c
            c = ans
        return ans