class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n, r, farthest, ans = len(nums), 0, 0, 0
        
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            
            if i == r:
                ans += 1
                r = farthest
        return ans