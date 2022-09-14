class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i, nums, dp):
            if i == 0:
                return nums[i]
            if i < 0: return 0
            if dp[i] != -1: return dp[i]
            
            pick = nums[i] + helper(i-2, nums, dp)
            not_pick = 0 + helper(i-1, nums, dp)
            dp[i] = max(pick, not_pick)
            return dp[i]

        dp = [-1]*len(nums)
        
        return helper(len(nums)-1, nums, dp)
            