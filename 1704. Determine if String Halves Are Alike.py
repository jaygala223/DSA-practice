class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt1, cnt2 = 0,0

        vowels = {'a', 'e', 'i','o','u', 'A', 'E', 'I','O','U'}
        

        for i in range(len(s)):
            if i < len(s)/2 and s[i] in vowels:
                cnt1 += 1
            elif s[i] in vowels:
                cnt2 += 1
        
        return cnt1 == cnt2
