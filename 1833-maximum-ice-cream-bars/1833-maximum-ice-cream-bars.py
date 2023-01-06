class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        
        for ic in costs:
            if ic <= coins:
                ans += 1
                coins -= ic
            else: break
        return ans