class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        freq, ans = {}, 0
        
        for item in tasks:
            freq[item] = freq.get(item, 0) + 1
        
        for item in freq:
            if freq[item] != 1:
                ans += (freq[item] + 2 )//3
            else:
                return -1
            
        return ans