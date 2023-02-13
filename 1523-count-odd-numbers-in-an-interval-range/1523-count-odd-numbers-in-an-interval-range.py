class Solution:
    def countOdds(self, low: int, high: int) -> int:
        wordsInBetween = high - low - 1
        ans = (wordsInBetween+1)//2
        
        if low%2 and high%2:
            ans = (wordsInBetween)//2
        
        
        if low%2: ans += 1
        if high%2: ans += 1
        
        return ans