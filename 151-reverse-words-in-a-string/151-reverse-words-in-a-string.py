class Solution:
    def reverseWords(self, s: str) -> str:
        #s.strip()
        words = s.split(' ')
        print(words)
        
        ans = ""
        for i in words:
            if(i != '' and i!= ' '):
                ans = i + ' ' + ans
        
        return ans.strip()