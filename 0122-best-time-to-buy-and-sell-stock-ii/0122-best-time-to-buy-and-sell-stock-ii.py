class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.dp = [[-1]*2]*len(prices)
        
        def f(ind, buy):
            #base
            if ind == len(prices): return 0
            if (ind, buy) in cache: return cache[(ind,buy)]
            
            profit = 0
            if buy:
                profit = max(f(ind+1, 0) - prices[ind], f(ind+1, 1) - 0)
            else:
                profit = max(f(ind+1, 1) + prices[ind], f(ind+1, 0) - 0)
                
            cache[(ind, buy)] = profit
            return profit
            
        #cache = dict()
        
        #space optimized bottom up
        n = len(prices)
        
        ahead_buy, ahead_not_buy = 0, 0
        
        for ind in range(n-1, -1, -1):
            curr_not_buy = max(prices[ind] + ahead_buy, ahead_not_buy)
            curr_buy = max(-prices[ind] + ahead_not_buy, ahead_buy)
            ahead_buy = curr_buy
            ahead_not_buy = curr_not_buy
            
        return ahead_buy
        
        #return f(0, 1)