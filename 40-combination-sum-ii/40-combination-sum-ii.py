class Solution:
    def helper(self, i, n, target, nums, subset, ans):
        
        if target == 0: 
            ans.append(subset[:])
            return
        
        for ind in range(i, n):
            #same value ignore
            if(ind > i and nums[ind] == nums[ind-1]): continue
            
            #ye value badi h to target nahi bana payegi...
            #and uske aage ke bhi bade honge
            if(nums[ind] > target): break
            
            subset.append(nums[ind])
            self.helper(ind+1, n, target-nums[ind], nums, subset, ans)
            subset.pop()

    
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        subset = []
        self.helper(0, n, target, candidates, subset, ans)
        return ans