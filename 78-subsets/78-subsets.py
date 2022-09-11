class Solution:
    def func(self, i, n, nums, subset, subs):
        if i > n-1:
            subs.append(subset[:])
            return
        
        subset.append(nums[i])
        self.func(i+1, n, nums, subset, subs)
        subset.pop()
        self.func(i+1, n, nums, subset, subs)
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subs = []
        subset = []
        self.func(0, n, nums, subset, subs)
        return subs