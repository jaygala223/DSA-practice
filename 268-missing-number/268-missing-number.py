class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for i in range(n):
            sum += nums[i]
            
        return int((n*(n+1))/2) - sum