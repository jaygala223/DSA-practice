class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        #TC: O(N) -> one traversal thru fruits
        #SC: O(N) -> dictionary
        
        ans, mp = 0, defaultdict(int)
        
        l, r = 0, 0
        
        while r < len(fruits):
            mp[fruits[r]] += 1
            
            if len(mp) <= 2:
                ans = max(ans, r-l+1)
            
            else:
                mp[fruits[l]] -= 1
                if mp[fruits[l]] < 1: mp.pop(fruits[l])
                l += 1
        
            r += 1
        return ans
                