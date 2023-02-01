class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini, maxi = int(1e9), -int(1e9)
        
        for n in nums:
            if n < mini: mini = n
            if n > maxi: maxi = n
        
        return gcd(maxi, mini)