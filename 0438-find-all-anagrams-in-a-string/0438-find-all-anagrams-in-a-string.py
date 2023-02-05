class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)
        
        freq_p = Counter(p)
        freq_s = defaultdict(int)
        
        for i in s[:n2]:
            freq_s[i] += 1
        
        l, r = 0, n2
        ans = []
        
        while r < n1:
            if freq_s == freq_p:
                ans.append(l)
            
            freq_s[s[l]] -= 1
            if freq_s[s[l]] < 1: freq_s.pop(s[l])
            
            freq_s[s[r]] += 1
            
            l += 1
            r += 1
        
        #while loop terminate hogaya last ind pe to...
        if freq_s == freq_p:
            ans.append(l)
        
        return ans