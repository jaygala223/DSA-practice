class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini, maxi = int(1e9), -int(1e9)
        
        def gCD(n1, n2):
            while n2:
                n1, n2 = n2, n1 % n2
            return abs(n1)
        
        for n in nums:
            if n < mini: mini = n
            if n > maxi: maxi = n
        
        return gCD(maxi, mini)