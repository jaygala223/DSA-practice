class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxi = max(candies)
        
        ans = []
        
        for c in candies:
            ans.append(c + extraCandies >= maxi)
            
        return ans