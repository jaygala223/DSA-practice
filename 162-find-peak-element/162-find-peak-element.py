class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        n = len(nums)
        hi = n-1
        
        #if(n == 1): return 0
        
        while(lo < hi):
            mid = int(lo + (hi-lo)/2)
            
            if(mid == n-1):
                return mid if nums[mid] >= nums[mid-1] else mid-1
                
            elif(mid == 0):
                return mid if nums[mid] >= nums[mid+1] else mid+1
            
            elif(nums[mid] >= nums[mid+1] and nums[mid] >= nums[mid-1]):
                return mid
            
            if(nums[mid] < nums[mid-1]): hi = mid-1;
            else: lo = mid+1
            
        return lo
        