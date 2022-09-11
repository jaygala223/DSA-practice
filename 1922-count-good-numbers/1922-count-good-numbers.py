class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        even = int(n/2) + n%2
        odd = n - even
        
        return pow(5, even, mod) * pow(4, odd, mod) % mod