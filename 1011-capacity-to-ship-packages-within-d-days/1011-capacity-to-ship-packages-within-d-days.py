class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #min and max capacity possible
        min_cap, max_cap = 0, 0
        
        for i in weights:
            if i > min_cap: min_cap = i
            max_cap += i
        
        ans = max_cap
        
        def check(val):
            d = 1
            currCap = val
            
            for i in weights:
                if currCap - i < 0:
                    currCap = val
                    d += 1
                currCap -= i
            
            return d <= days
        
        while min_cap <= max_cap:
            capacity = (min_cap + max_cap) // 2
            
            if check(capacity):
                ans = min(ans, capacity)
                max_cap = capacity - 1
            else:
                min_cap = capacity + 1
        
        return ans