class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        n = len(nums)
        hi = n-1
        
        #if(n == 1): return 0
        
        while(lo < hi):
            mid = int(lo + (hi-lo)/2)
            
            if(nums[mid] < nums[mid+1]):
                lo = mid+1
            else: hi = mid
            
        return lo
        