class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        tot = sum(nums)
        
        min_sub, max_sub = [100000], [-1000000]
        
        def kadane(nums, cur_max, cur_min):
            for num in nums:
                if cur_max < 0:
                    cur_max = 0
                if cur_min > 0:
                    cur_min = 0
                cur_max, cur_min = cur_max + num, cur_min + num
                min_sub[0] = min(min_sub[0], cur_min)
                max_sub[0] = max(max_sub[0], cur_max)
        
        kadane(nums, 0, 0)
        if tot == min_sub[0]: return max_sub[0]
        print(min_sub[0], max_sub[0])
        return max(tot - min_sub[0], max_sub[0])