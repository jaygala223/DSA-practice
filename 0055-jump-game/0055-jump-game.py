class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach, i = 0, 0
        
        while(i < len(nums)):
            if i > reach:
                break
            reach = max(reach, i + nums[i])
            i+=1
            
        return i == len(nums)