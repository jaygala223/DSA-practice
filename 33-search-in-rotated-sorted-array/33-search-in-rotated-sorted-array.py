class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        
        while(lo <= hi):
            mid = lo + int((hi-lo)/2)
            
            if(nums[mid] == target): return mid;
            
            elif(nums[lo] <= nums[mid]):
                if(nums[lo] <= target and nums[mid] >= target):
                    hi = mid-1
                else: lo = mid+1
            
            else:
                if(nums[mid] <= target and nums[hi] >= target):
                    lo = mid+1
                else: hi = mid-1
            
        else: return -1