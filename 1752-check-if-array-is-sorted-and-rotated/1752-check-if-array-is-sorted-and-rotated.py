class Solution:
    def check(self, nums: List[int]) -> bool:
        
        count = 0
        
        for i in range(1, len(nums)):
            if(nums[i] < nums[i-1]):
                count+=1
        
        if count == 0: return True
        else: return count == 1 and nums[0] >= nums[-1]