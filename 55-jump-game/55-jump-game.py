class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = nums[-1]
        
        for i in range(len(nums)-1, -1, -1):
            last = i if i+nums[i] >= last else last
                
        return last == 0