class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        
        #https://leetcode.com/problems/minimum-cost-to-split-an-array/discuss/3083951/Python-Simple-DP-with-Dict-(Hashmap)-15-Lines-of-code
        
        #TC: O(N*N) -> recursive and iterative loop
        #SC: O(N) -> HashMap
        
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