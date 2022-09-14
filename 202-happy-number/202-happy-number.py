class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumAndSquare(n):
            add = 0
            
            while n:
                add += (n%10)**2
                n = n//10
            return add
            
        slow = sumAndSquare(n)
        fast = sumAndSquare(sumAndSquare(n))
        
        while slow != fast:
            slow = sumAndSquare(slow)
            fast = sumAndSquare(fast)
            fast = sumAndSquare(fast)
        return fast == 1
        