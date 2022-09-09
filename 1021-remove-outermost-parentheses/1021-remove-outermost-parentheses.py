class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        ans, opened = "", 0
        
        for c in s:
            if c == '(' and opened > 0: ans += c
            elif c == ')' and opened > 1: ans += c
            
            opened += 1 if c == '(' else -1
        
        return ans