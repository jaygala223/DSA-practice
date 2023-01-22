class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        
        @cache
        def dp(ind):
            if ind == len(nums):
                return 0
            
            m = float('inf')
            
            counter = defaultdict(int)
            count = 0
            
            for j in range(ind, len(nums)):
                counter[nums[j]] += 1
                
                if counter[nums[j]] > 2:
                    count += 1
                
                elif counter[nums[j]] == 2:
                    count += 2
                
                imp = k + count
                m = min(imp + dp(j+1), m)
            
            return m
        
        return dp(0)