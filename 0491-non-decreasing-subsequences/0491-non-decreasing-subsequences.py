class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def subs(ind, prev, curr):
            if ind >= len(nums):
                if len(curr) > 1: 
                    res.add(tuple(curr))
                return
            
            if nums[ind] >= prev:
                #add to curr subsequence
                #pick
                curr.append(nums[ind])
                subs(ind+1, nums[ind], curr)
                curr.pop()
            
            #not pick
            subs(ind+1, prev, curr)
        
        subs(0, -10000, [])
        return res