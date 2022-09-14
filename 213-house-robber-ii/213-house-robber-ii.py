class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def robhouses(nums):
            n = len(nums)
            dp = [0]*n
            dp[0] = nums[0]
            for i in range(1, n):
                pick = nums[i]
                if i>1: pick += dp[i-2]
                not_pick = 0 + dp[i-1]
                dp[i] = max(pick, not_pick)
            return dp[n-1]
        
        return max(robhouses(nums[1:]), robhouses(nums[:n-1]))