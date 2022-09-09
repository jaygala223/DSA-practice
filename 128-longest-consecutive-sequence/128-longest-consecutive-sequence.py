class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums)==0): return 0
        
        nums = set(nums)
        cnt = 0
        ans = 0
        for item in nums:
            
            #start of sequence
            if item-1 not in nums:
                cnt = 1
                while item+1 in nums:
                    item +=1
                    cnt+=1
            ans = max(cnt, ans)
        
        
        return ans;
            