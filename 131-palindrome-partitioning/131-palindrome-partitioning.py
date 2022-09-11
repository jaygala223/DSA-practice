class Solution:
    def isPali(self, s):
        l,r = 0, len(s)-1
        while(l <= r):
            if s[l] != s[r]: return False
            l+=1
            r-=1
        return True
    
    
    def func(self, i, n, s, ds, ans):
        if i > n-1:
            ans.append(ds[:])
        
        for j in range(i, n):
            
            if(self.isPali(s[i:j+1])):
                sub = s[i:j+1]
                ds.append(sub)
                self.func(j+1, n, s, ds, ans)
                ds.pop()
    
    
    def partition(self, s: str) -> List[List[str]]:
        ds = []
        ans = []
        
        n = len(s)
        self.func(0, n, s, ds, ans)
        return ans