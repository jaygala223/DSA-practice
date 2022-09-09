class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = 10e6
        
        for i in prices:
            mini = min(mini, i)
            profit = max(i-mini, profit)
        
        
        return profit