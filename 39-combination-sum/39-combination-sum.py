class Solution:
    def helper(self, i, n, target, nums, subset, ans):
        
        if i > n-1:
            if target == 0: ans.append(subset[:])
            return
        
        if nums[i] <= target:
            subset.append(nums[i])
            self.helper(i, n, target-nums[i], nums, subset, ans)
            subset.pop()
        
        
        self.helper(i+1, n, target, nums, subset, ans)
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        ans = []
        subset = []
        self.helper(0, n, target, candidates, subset, ans)
        return ans