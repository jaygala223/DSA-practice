class Solution:
    def func(self, i, n, nums, subset, ans):
        
        ans.append(subset[:])
        
        for ind in range(i, n):
            #to avoid duplicates
            if ind>i and nums[ind] == nums[ind-1]: continue
            
            subset.append(nums[ind])
            self.func(ind+1, n, nums, subset, ans)
            subset.pop()
            
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        subset = []
        self.func(0, n, nums, subset, ans)
        return ans