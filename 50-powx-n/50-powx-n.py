class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1: return x
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -1*n)
        
        lower = self.myPow(x, n//2)
        if n%2 == 0: return lower*lower
        else: return lower*lower*x