class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        nums = sorted(nums)
        
        return (nums[0]*10 + nums[2]) + (nums[1]*10 + nums[3])
        