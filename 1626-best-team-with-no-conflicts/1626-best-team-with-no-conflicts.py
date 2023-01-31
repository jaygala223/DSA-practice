class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #can be thought of as a LIS problem
        #recursive tc: 2^n ... similar to subsequences problem
        #memo: n^2
        
        n = len(ages)
        ans = -1e9
        
        players = [[s, a] for a, s in zip(ages, scores)]
        players.sort()
        
        dp = {}
        
        def func(ind, maxAge):
            if ind == n:
                return 0
            
            if (ind, maxAge) in dp:
                return dp[(ind, maxAge)]
            
            curr_age = players[ind][1]
            curr_score = players[ind][0]
            
            take, not_take = 0, 0
            
            if curr_age >= maxAge:
                take = curr_score + func(ind + 1, curr_age)
                # not_take = 0 + func(ind + 1, maxAge)
                # dp[(ind, maxAge)] = max(take, not_take)
                # return max(take, not_take)
                
            not_take = 0 + func(ind + 1, maxAge)
            dp[(ind, maxAge)] = max(take, not_take)
            return max(take, not_take)
        
        return func(0, 0)
        