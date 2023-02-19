class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        
        dp = {}
        
        ptr, kIndex = 0, 0
        
        #note: ptr points to the current DIAL position.
        
        def func(ptr, kIndex):
            if kIndex == m: return 0
            if (ptr, kIndex) in dp: return dp[(ptr, kIndex)]
            
            steps = 1e9
            
            for i in range(n):
                if ring[i] == key[kIndex]:
                    steps = min(steps, n-abs(i-ptr) + 1 + func(i, kIndex+1))
                    steps = min(steps, abs(i-ptr) + 1 + func(i, kIndex+1))
            
            dp[(ptr, kIndex)] = steps
            return dp[(ptr, kIndex)]
        
        return func(ptr, kIndex)