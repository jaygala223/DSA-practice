class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        
        for s in stones:
            if s in jewels:
                ans += 1
                
        return ans