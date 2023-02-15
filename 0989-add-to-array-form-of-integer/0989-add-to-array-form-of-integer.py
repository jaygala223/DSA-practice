class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        ans = []
        num = reversed(num)
        carry = 0
        
        for i in num:
            curr_sum = carry
            curr_sum += i
            if k: 
                curr_sum += k%10
                k = k//10
            
            ans.append(curr_sum%10)
            
            if curr_sum >= 10:
                carry = curr_sum//10
            else: carry = 0
        
        while k:
            new_sum = carry
            new_sum += k%10
            k = k//10
            ans.append(new_sum%10)
            if new_sum >= 10:
                carry = new_sum//10
            else: carry = 0
        
        if carry:
            ans.append(carry)
        
        return ans[::-1]
                
                