class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        ans = 0
        
        suffixes = [set() for _ in range(26)] #sets for all chars
        for idea in ideas:
            suffixes[ord(idea[0]) - ord('a')].add(idea[1:])
        
        for i in range(25):
            for j in range(i+1, 26):
                k = len(suffixes[i] & suffixes[j]) #no. of duplicates in both sets
                ans += 2 * (len(suffixes[i]) - k) * (len(suffixes[j]) - k)
        
        return ans