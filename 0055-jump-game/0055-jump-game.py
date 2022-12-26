class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        
        reach, i = 0, 0
        
        while(i < n):
            if i > reach:
                break
            reach = max(reach, i + nums[i])
            i+=1
            
        return i == n