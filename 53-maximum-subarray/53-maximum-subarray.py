class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        ans = int(-10e9)
        
        for i in nums:
            if(curr_sum < 0):
                curr_sum = 0
            curr_sum += i
            
            ans = max(curr_sum, ans)
        
        return ans