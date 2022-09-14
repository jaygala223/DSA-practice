class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def robhouses(nums):
            rob1, rob2 = 0,0
            
            for item in nums:
                temp = max(item + rob1, rob2)
                rob1 = rob2
                rob2 = temp
                
            return rob2
        
        return max(robhouses(nums[1:]), robhouses(nums[:n-1]))