class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        ans = ""
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        #returns a list sorted by the freq of the letters
        sorted_freq = sorted(freq, key=freq.get, reverse=True)
        print(sorted_freq)
        
        for i in sorted_freq:    
            ans += (i * freq[i])
        
        return ans
            