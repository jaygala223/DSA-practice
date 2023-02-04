class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #TC: O(2n)--> O(N + M) => two traversals
        #SC: O(2n) --> O(N)
        
        n1, n2 = len(s1), len(s2)
        
        if n2 < n1:
            return False

        ctr1 = defaultdict(int)
        ctr2 = defaultdict(int)
        
        for i in s1: ctr1[i] += 1
        for x in s2[:n1]: ctr2[x] += 1
        
        l = 0
        r = n1
        
        while r < n2:
            if ctr1 == ctr2: return True
            
            ctr2[s2[l]] -= 1
            if ctr2[s2[l]] < 1: ctr2.pop(s2[l])
            
            ctr2[s2[r]] += 1
            
            l += 1
            r += 1
        
        return ctr1 == ctr2