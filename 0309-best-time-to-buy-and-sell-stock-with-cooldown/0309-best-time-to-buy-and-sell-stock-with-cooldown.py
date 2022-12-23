class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        def f(ind, buy):
            #base
            if ind >= len(prices): return 0
            if (ind, buy) in cache: return cache[(ind,buy)]
            
            profit = 0
            if buy:
                profit = max(f(ind+1, 0) - prices[ind], f(ind+1, 1) - 0)
            else:
                profit = max(f(ind+2, 1) + prices[ind], f(ind+1, 0) - 0)
                
            cache[(ind, buy)] = profit
            return profit
        
        cache = dict()
        return f(0, 1)
        
        
        
        #space optimized bottom up
        
        