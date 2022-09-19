class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {
            ')':'(',']':'[','}':'{'
        }
        
        for i in s:
            if i in "([{": stack.append(i)
            else:
                if stack != [] and pairs[i] == stack.pop():
                    continue
                    
                else: return False
        return stack == []