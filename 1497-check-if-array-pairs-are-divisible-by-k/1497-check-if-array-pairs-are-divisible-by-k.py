class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        if len(arr) % 2 == 1: return False
        
        lookup = collections.defaultdict(int)
        count = 0
        
        for num in arr:
            key = k - (num % k)
            if key in lookup and lookup[key] >= 1:
                count += 1
                lookup[key] -= 1
            else:
                #-3 agaya and k==3 hua to .. seedha 3 rakh not ZERO
                lookup[(num % k) or k] += 1
        return count == len(arr) // 2