class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        if m != n: return False
        
        freq = [0]*26
        
        for c in s:
            freq[ord(c) -ord('a')] += 1
        
        for c in t:
            freq[ord(c)-ord('a')] -= 1
            
        return True if max(freq) == 0 else False
            
        